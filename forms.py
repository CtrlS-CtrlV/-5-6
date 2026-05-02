from django import forms
from django.core.exceptions import ValidationError

class ConferenceRegistrationForm(forms.Form):
    name = forms.CharField(label="Ваше ім'я", max_length=100)
    email = forms.EmailField(label="Електронна пошта")
    topic = forms.ChoiceField(label="Секція", choices=[
        ('dev', 'Розробка'), ('qa', 'Тестування'), ('pm', 'Менеджмент')
    ])
    message = forms.CharField(label="Тези доповіді", widget=forms.Textarea)

    # Кастомна валідація
    def clean_message(self):
        data = self.cleaned_data['message']
        if len(data.split()) < 5:
            raise ValidationError("Тези мають містити принаймні 5 слів!")
        return data
