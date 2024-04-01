from django import forms
from django.core.exceptions import ValidationError

from Account.models import CustomUser
from Account.validator_utilities import validate_mobile_phone_handler, validate_username_handler, \
    validate_passwords_handler, validate_full_name_handler, validate_company_name_handler


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")
    password_repeat = forms.CharField(widget=forms.PasswordInput, label="تکرار رمز عبور")

    class Meta:
        model = CustomUser
        fields = ("mobile_phone", "full_name", "company_name", "password", "password_repeat")

    def clean_mobile_phone(self):
        mobile_phone = self.cleaned_data.get("mobile_phone")

        has_errors = validate_mobile_phone_handler(mobile_phone=mobile_phone).get("has_errors")
        message = validate_mobile_phone_handler(mobile_phone=mobile_phone).get("message")
        code = validate_mobile_phone_handler(mobile_phone=mobile_phone).get("code")

        if has_errors:
            raise ValidationError(message=message, code=code)
        else:
            return mobile_phone

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")

        has_errors = validate_full_name_handler(full_name=full_name).get("has_errors")
        message = validate_full_name_handler(full_name=full_name).get("message")
        code = validate_full_name_handler(full_name=full_name).get("code")

        if has_errors:
            raise ValidationError(message=message, code=code)
        else:
            return full_name

    def clean_company_name(self):
        company_name = self.cleaned_data.get("company_name")

        has_errors = validate_company_name_handler(company_name=company_name).get("has_errors")
        message = validate_company_name_handler(company_name=company_name).get("message")
        code = validate_company_name_handler(company_name=company_name).get("code")

        if has_errors:
            raise ValidationError(message=message, code=code)
        else:
            return company_name

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")

        has_errors = validate_passwords_handler(password=password, password_repeat=password_repeat).get("has_errors")
        message = validate_passwords_handler(password=password, password_repeat=password_repeat).get("message")
        code = validate_passwords_handler(password=password, password_repeat=password_repeat).get("code")

        if has_errors:
            raise ValidationError(message=message, code=code)


class LogInForm(forms.Form):
    mobile_phone = forms.CharField(max_length=75, label="شماره تفلن")
    password = forms.CharField(widget=forms.PasswordInput(), label="رمز عبور")

    def clean(self):
        mobile_phone = self.cleaned_data.get("mobile_phone")

        try:
            CustomUser.objects.get(mobile_phone=mobile_phone)

            has_errors = validate_mobile_phone_handler(mobile_phone=mobile_phone,
                                                       mobile_phone_exists_importance=False).get("has_errors")
            message = validate_mobile_phone_handler(mobile_phone=mobile_phone,
                                                    mobile_phone_exists_importance=False).get("message")
            code = validate_mobile_phone_handler(mobile_phone=mobile_phone,
                                                 mobile_phone_exists_importance=False).get("code")
            if has_errors:
                raise ValidationError(message=message, code=code)

        except CustomUser.DoesNotExist:
            message = "کاربری با این مشخصات یافت نشد."
            code = "does_not_exist"

            raise ValidationError(message=message, code=code)


class CheckOTPForm(forms.Form):
    sms_code = forms.CharField(max_length=4, widget=forms.TextInput(
        attrs={'pattern': '[0-9]*', 'oninput': 'this.value = this.value.replace(/[^0-9]/g, "")'}), label="کد تایید")


class ForgetPasswordForm(forms.Form):
    mobile_phone = forms.CharField(max_length=75, label="شماره تلفن")

    def clean(self):
        mobile_phone = self.cleaned_data.get("mobile_phone")

        try:
            CustomUser.objects.get(mobile_phone=mobile_phone)

            has_errors = validate_mobile_phone_handler(mobile_phone=mobile_phone,
                                                       mobile_phone_exists_importance=False).get("has_errors")
            message = validate_mobile_phone_handler(mobile_phone=mobile_phone,
                                                    mobile_phone_exists_importance=False).get("message")
            code = validate_mobile_phone_handler(mobile_phone=mobile_phone,
                                                 mobile_phone_exists_importance=False).get("code")
            if has_errors:
                raise ValidationError(message=message, code=code)

        except CustomUser.DoesNotExist:
            message = "کاربری با این مشخصات یافت نشد."
            code = "does_not_exist"

            raise ValidationError(message=message, code=code)


class ChangePasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(), label="رمز عبور")

    password_repeat = forms.CharField(
        widget=forms.PasswordInput(), label="تکرار رمز عبور")

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        password_repeat = cleaned_data.get("password_repeat")

        has_errors = validate_passwords_handler(password=password, password_repeat=password_repeat).get("has_errors")
        message = validate_passwords_handler(password=password, password_repeat=password_repeat).get("message")
        code = validate_passwords_handler(password=password, password_repeat=password_repeat).get("code")

        if has_errors:
            raise ValidationError(message=message, code=code)
