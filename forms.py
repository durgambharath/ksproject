from django import forms
from watersupply.models import quater1_watersupply
class quater1_watersupplyForm(forms.ModelForm):
    class Meta:
        model = quater1_watersupply
        fields = "__all__"
