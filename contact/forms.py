from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        required=True,
        widget=forms.TextInput(attrs={'class': 'fh5co_contact_form', 'placeholder': "Escribe tu Nombre"}),
        min_length=3,
        max_length=100
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={'class': 'fh5co_contact_form', 'placeholder': "Escribe tu Email"})
    )
    message = forms.CharField(
        label="Mensaje",
        required=True,
        widget=forms.Textarea(attrs={'class': 'fh5co_contact_form', 'rows': 3, 'placeholder': "Escribe tu Mensaje"}),
        min_length=10,
        max_length=1000
    )
