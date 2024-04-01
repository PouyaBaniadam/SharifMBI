from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView, ListView, DetailView

from Account.models import CustomUser
from Us.forms import ContactForm
from Us.models import AboutUs, Customer


class About(TemplateView):
    template_name = "Us/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        about = AboutUs.objects.last()

        context['about'] = about

        return context


class Contact(FormView):
    form_class = ContactForm
    template_name = "Us/contact.html"
    success_url = "/"

    def get_form_kwargs(self):
        kwargs = super(Contact, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        user = CustomUser.objects.get(username=self.request.user.username)
        print(user.mobile_phone)

        message = form.cleaned_data.get("message")

        if user.is_authenticated:
            mobile_phone = form.cleaned_data.get("mobile_phone", user.mobile_phone)
            email = form.cleaned_data.get("email", user.email)
            full_name = form.cleaned_data.get("full_name", user.full_name)

            if mobile_phone is None:
                mobile_phone = user.mobile_phone

            if email is None:
                email = user.email

            if full_name is None:
                full_name = user.full_name

            instance = form.save(commit=False)

            instance.user = user
            instance.mobile_phone = mobile_phone
            instance.email = email
            instance.full_name = full_name

            instance.save()

        else:
            mobile_phone = form.cleaned_data.get("mobile_phone")
            email = form.cleaned_data.get("email")
            full_name = form.cleaned_data.get("full_name")

            form.instance.user = user
            form.instance.mobile_phone = mobile_phone
            form.instance.email = email
            form.instance.full_name = full_name
            form.instance.message = message

        messages.success(self.request, "پیام شما با موقیت ثبت شد.")

        return redirect("us:contact")


class CustomerList(ListView):
    model = Customer
    context_object_name = "customers"
    template_name = "Us/customers.html"


class CustomerDetail(DetailView):
    model = Customer
    context_object_name = "customer"
    template_name = "Us/customer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        current_customer = self.get_object()

        customers = Customer.objects.exclude(pk=current_customer.pk)

        context['customers'] = customers

        return context
