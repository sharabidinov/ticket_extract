from django import forms
from .models import Ticket, Flight


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = '__all__'


FlightFormSet = forms.inlineformset_factory(Ticket, Flight, form=FlightForm, extra=1, can_delete_extra=True)
