from django.urls import path

from Account import views

app_name = "account"

urlpatterns = [
    path("profile/<slug:slug>", views.ProfileDetailView.as_view(), name="profile"),
    path("profile/<slug:slug>/edit", views.ProfileEditView.as_view(), name="edit_profile"),
    path("login", views.LogInView.as_view(), name="login"),
    path("register", views.OTPRegisterView.as_view(), name="register"),
    path("logout", views.LogOutView.as_view(), name="logout"),
    path("check/otp", views.CheckOTPView.as_view(), name="check_otp"),
    path("password/forget", views.ForgetPasswordView.as_view(), name="forget_password"),
    path("password/change", views.ChangePasswordView.as_view(), name="change_password"),
    path("notifications", views.NotificationListView.as_view(), name="notifications"),
]
