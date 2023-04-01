from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import UseInfo


class UserInfoForm(forms.ModelForm):
    mailbox = forms.EmailField(label='邮箱', required=True)
    phone_number = PhoneNumberField(label='手机号', required=True)

    class Meta:
        model = UseInfo
        fields = "__all__"
