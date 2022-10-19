from random import choices
from socket import fromshare
from django import forms
class OrderUpdateForm(forms.Form):
    options=(
        ("dispatched","dispatched"),
        ("in-transit","in-transit")
    )
    status=forms.ChoiceField(choices=options,widget=forms.Select(attrs={"class":"form-select"}))
    expected_delivery_date=forms.DateField(widget=forms.DateInput(attrs={"class":"form-control","type":"date"}))
