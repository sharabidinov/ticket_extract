from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from .models import Ticket, Flight
from .forms import TicketForm, FlightFormSet


class TicketInline:
    form_class = TicketForm
    model = Ticket
    template_name = 'ticket/ticket_create_update.html'

    def form_valid(self, form):
        named_formsets = self.get_named_formsets()
        if not all((x.is_valid() for x in named_formsets.values())):
            return self.render_to_response(self.get_context_data(form=form))

        self.object = form.save()

        for name, formset in named_formsets.items():
            formset_value_func = getattr(self, 'formset_{0}_valid'.format(name), None)
            if formset_value_func is not None:
                formset_value_func(formset)
            else:
                formset.save()

            return redirect('ticket:list_tickets')

    def flight_formset_valid(self, formset):
        flights = self.save_formset(formset, contact)  # formset.save(commit=False)

        for obj in formset.deleted_objects:
            obj.delete()
        for flight in flights:
            flight.ticket = self.object
            flight.save()


class TicketCreate(TicketInline, CreateView):
    def get_context_data(self, **kwargs):
        ctx = super(TicketCreate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        if self.request.method == "GET":
            return {
                'flights': FlightFormSet(prefix='flights'),
            }
        else:
            return {
                'flights': FlightFormSet(self.request.POST or None, self.request.FILES or None, prefix='flights')
            }


class TicketUpdate(TicketInline, UpdateView):
    def get_context_data(self, **kwargs):
        ctx = super(TicketUpdate, self).get_context_data(**kwargs)
        ctx['named_formsets'] = self.get_named_formsets()
        return ctx

    def get_named_formsets(self):
        return {
            'flights': FlightFormSet(self.request.POST or None, self.request.FILES or None, instance=self.object,
                                     prefix='flights'),
        }


class TicketList(ListView):
    model = Ticket
    template_name = 'ticket/ticket_list.html'
    context_object_name = 'tickets'


def delete_ticket(request, pk):
    try:
        flight = Flight.objects.get(id=pk)
    except Flight.DoesNotExist:
        messages.success(
            request, 'Object Does not exit'
        )
        return redirect('tickets:update_product', pk=flight.product.id)

    flight.delete()
    messages.success(
        request, 'Flight deleted successfully'
    )
    return redirect('tickets:update_product', pk=flight.product.id)
