import random
from uuid import uuid4

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import FormView

from Account.forms import RegisterForm, CheckOTPForm, LogInForm, ForgetPasswordForm, ChangePasswordForm
from Account.mixins import NonAuthenticatedUsersOnlyMixin
from Account.models import CustomUser, OTP
from Home.sms import send_forget_password_sms


class OTPRegisterView(FormView):
    template_name = "Account/register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        sms_code = random.randint(a=1000, b=9999)
        mobile_phone = form.cleaned_data.get('mobile_phone')
        full_name = form.cleaned_data.get('full_name')
        company_name = form.cleaned_data.get('company_name')
        password = form.cleaned_data.get('password')
        uuid = str(uuid4())

        OTP.objects.create(mobile_phone=mobile_phone, sms_code=sms_code, uuid=uuid, full_name=full_name,
                           password=password, company_name=company_name, otp_type="R")

        # send_register_sms(receptor=mobile_phone, sms_code=sms_code)
        print(sms_code)

        return redirect(reverse("account:check_otp") + f"?uuid={uuid}&mobile_phone={mobile_phone}")

    def form_invalid(self, form):
        return super().form_invalid(form)


class LogInView(NonAuthenticatedUsersOnlyMixin, FormView):
    form_class = LogInForm
    template_name = 'Account/login.html'

    def form_valid(self, form):
        request = self.request
        mobile_phone = form.cleaned_data.get('mobile_phone')
        password = form.cleaned_data.get('password')

        user = CustomUser.objects.get(mobile_phone=mobile_phone)

        authenticated_user = authenticate(request=request, mobile_phone=mobile_phone, password=password)

        if authenticated_user is not None:
            login(request=request, user=user)

        else:
            form.add_error(field="mobile_phone", error="هیچ حساب کاربری با این مشخصات یافت نشد.")

            return self.form_invalid(form)

        messages.success(request=request, message=f"{user.full_name} عزیز، خوش آمدید. ")

        return redirect(reverse("home:home"))

    def get_success_url(self):
        referring_url = self.request.session.pop(key="referring_url", default=None)
        return referring_url or reverse_lazy("home:home")


class LogOutView(View):
    def get(self, request):
        logout(request=request)
        next_url = request.GET.get("next")

        if next_url is not None:
            messages.success(request=request, message=f"شما با موفقیت از حساب کاربری خود خارج شدید.")
            return redirect(next_url)

        else:
            try:
                messages.success(request=request, message=f"شما با موفقیت از حساب کاربری خود خارج شدید.")

                home_url = reverse('home:home')

                return redirect(home_url)

            except:
                messages.success(request=request, message=f"شما با موفقیت از حساب کاربری خود خارج شدید.")

                return redirect(to="home:home")


class ChangePasswordView(NonAuthenticatedUsersOnlyMixin, FormView):
    form_class = ChangePasswordForm
    template_name = 'Account/change_password.html'

    def form_valid(self, form):
        request = self.request
        new_password = form.cleaned_data.get('password')
        uuid = request.GET.get('uuid')

        otp = OTP.objects.get(uuid=uuid)
        mobile_phone = otp.mobile_phone

        user = CustomUser.objects.get(mobile_phone=mobile_phone)

        user.set_password(raw_password=new_password)
        user.save()

        login(request=request, user=user)

        otp.delete()

        messages.success(request=request, message=f"رمز عبور با موفقیت تغییر یافت.")

        return redirect(reverse('home:home'))

    def form_invalid(self, form):
        return super().form_invalid(form)


class ForgetPasswordView(NonAuthenticatedUsersOnlyMixin, FormView):
    form_class = ForgetPasswordForm
    template_name = "Account/forget_password.html"

    def form_valid(self, form):
        mobile_phone = form.cleaned_data.get('mobile_phone')

        user = CustomUser.objects.get(mobile_phone=mobile_phone)

        mobile_phone = user.mobile_phone

        sms_code = random.randint(a=1000, b=9999)
        uuid = str(uuid4())

        OTP.objects.create(mobile_phone=mobile_phone, sms_code=sms_code, uuid=uuid,
                           otp_type="F")

        # send_forget_password_sms(receptor=mobile_phone, sms_code=sms_code)

        print(sms_code)

        return redirect(reverse(viewname="account:check_otp") + f"?uuid={uuid}&mobile_phone={mobile_phone}")

    def form_invalid(self, form):
        return super().form_invalid(form)


class CheckOTPView(FormView):
    form_class = CheckOTPForm
    template_name = 'Account/check_otp.html'

    def form_valid(self, form):
        request = self.request
        uuid = request.GET.get('uuid')
        sms_code = form.cleaned_data.get('sms_code')

        if OTP.objects.filter(uuid=uuid, sms_code=sms_code, otp_type="R").exists():
            otp = OTP.objects.get(uuid=uuid)

            mobile_phone = otp.mobile_phone
            username = otp.username
            password = otp.password

            user = CustomUser.objects.create_user(mobile_phone=mobile_phone, username=username)

            user.set_password(password)
            user.full_name = otp.full_name
            user.save()

            login(request=request, user=user)

            otp = OTP.objects.get(uuid=uuid)
            otp.delete()

            messages.success(request=request, message=f"{user.full_name} عزیز. حساب شما با موفقیت ساخته شد.")

            return redirect(to="home:home")

        elif OTP.objects.filter(uuid=uuid, sms_code=sms_code, otp_type="F").exists():

            return redirect(reverse(viewname="account:change_password") + f"?uuid={uuid}")

        elif OTP.objects.filter(uuid=uuid, sms_code=sms_code, otp_type="D").exists():
            otp = OTP.objects.get(uuid=uuid)
            username = otp.username

            user_to_be_deleted = CustomUser.objects.get(username=username)

            user_to_be_deleted.delete()
            otp.delete()

            return redirect(to="home:home")

        else:
            form.add_error(field="sms_code", error="کد تایید نامعتبر است.")

            return self.form_invalid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
