from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse


class NonAuthenticatedUsersOnlyMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home:home")
        return super(NonAuthenticatedUsersOnlyMixin, self).dispatch(request, *args, **kwargs)


class AuthenticatedUsersOnlyMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            referring_url = request.META.get('HTTP_REFERER', None)
            request.session['referring_url'] = referring_url

            messages.error(request, "این بخش فقط مخصوص کاربران ثبت نام شده است.")
            return redirect("home:home")

        return super(AuthenticatedUsersOnlyMixin, self).dispatch(request, *args, **kwargs)
