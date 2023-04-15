from django import forms
from phonenumber_field.formfields import PhoneNumberField
from ckeditor_uploader.fields import RichTextUploadingFormField
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import UseInfo


class UserInfoForm(forms.ModelForm):
    mailbox = forms.EmailField(label='邮箱', required=True)
    phone_number = PhoneNumberField(label='手机号', required=True)
    introduction = RichTextUploadingFormField(widget=CKEditorUploadingWidget, label='个人简介', required=True,
                                              config_name="default")

    class Meta:
        model = UseInfo
        fields = ['mailbox', 'phone_number']
