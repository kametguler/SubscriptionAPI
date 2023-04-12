from django import forms
from shopping.models import BillingInformation
from shopping.models import Cities
import phonenumbers
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class CheckoutForm(forms.ModelForm):
    phone = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255)
    city = forms.ModelChoiceField(
        queryset=Cities.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )

    class Meta:
        model = BillingInformation
        exclude = ['order', 'country', 'email']

    def __init__(self, *args, **kwargs):
        super(CheckoutForm, self).__init__(*args, **kwargs)
        self.fields['city'].label = 'Şehir'
        self.fields['phone'].label = 'Telefon'
        self.fields['full_name'].label = 'İsim Soyisim'
        self.fields['address'].label = 'Adres'
        self.fields['postal_code'].label = 'Posta Kodu'
        self.fields['full_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['postal_code'].widget.attrs.update({'class': 'form-control'})

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
