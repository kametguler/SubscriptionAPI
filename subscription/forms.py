import phonenumbers
from django import forms
from subscription.models.product import ProductFeedback
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Tam İsim", required=True)
    email = forms.EmailField(max_length=100, label="Email", required=True)
    phone = forms.CharField(max_length=15, label="Telefon numarası", required=True)
    message = forms.CharField(widget=forms.Textarea, label="Mesaj", required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update({'class': 'form-control', 'placeholder': "Tam adınız"})
        self.fields["email"].widget.attrs.update({'class': 'form-control', 'placeholder': "Email adresiniz"})
        self.fields["phone"].widget.attrs.update({'class': 'form-control', 'placeholder': "5554443322"})
        self.fields["message"].widget.attrs.update(
            {'rows': 10, 'placeholder': "Konudan bahsediniz", "cols": 30, "class": "form-control"})

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        phone = self.cleaned_data["phone"]
        send_mail(
            'İletişim Formu Gönderimi Alındı - {0}'.format(name),
            message + "\n\nTelefon Numarası:" + phone,
            email,
            ['your_email@example.com'],
            fail_silently=False,
        )

    def clean_phone(self):
        """
        Validate phone number.
        """
        phone = self.cleaned_data['phone']
        if phone[0] == "0":
            phone += f"+9{phone}"
        elif phone[0] == "5":
            phone = f"+90{phone}"
        try:
            parsed_phone = phonenumbers.parse(phone, "TR")
        except phonenumbers.NumberParseException:
            raise ValidationError(_("Hatalı telefon numarası."))

        if not phonenumbers.is_valid_number(parsed_phone):
            raise ValidationError(_("Hatalı telefon numarası."))

        return phone


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = ProductFeedback
        fields = ('rating', 'comment')
        widgets = {'rating': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields["comment"].widget.attrs.update({'class': 'form-control', 'rows': 5})
        self.fields["rating"].widget.attrs.update({'value': "5"})
