from django import forms


class AddGroupClassForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=[(i, str(i)) for i in range(1, 8)], coerce=int)
    update = forms.BooleanField(
        required=False, initial=False, help_text="Update quantity or add to previous value?")