from django.urls import path

from Account import views

app_name = "account"

urlpatterns = [
    path("login", views.LogInView.as_view(), name="login"),
    path("register", views.OTPRegisterView.as_view(), name="register"),
    path("logout", views.LogOutView.as_view(), name="logout"),
    path("check/otp", views.CheckOTPView.as_view(), name="check_otp"),
    path("password/forget", views.ForgetPasswordView.as_view(), name="forget_password"),
    path("password/change", views.ChangePasswordView.as_view(), name="change_password"),
]
