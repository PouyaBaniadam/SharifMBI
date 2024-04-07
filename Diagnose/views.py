import os

from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import FormView, View

from Account.mixins import AuthenticatedUsersOnlyMixin
from Diagnose.forms import DiagnoseForm
from Home.mixins import URLStorageMixin
from SharifMBI import settings


class DiagnoseFormView(URLStorageMixin, AuthenticatedUsersOnlyMixin, FormView):
    form_class = DiagnoseForm
    template_name = 'Diagnose/diagnose_form.html'
    success_url = '/'

    def form_valid(self, form):
        request = self.request

        instance = form.save(commit=False)
        instance.user = request.user

        instance.save()

        messages.success(request=request, message=f"فرم عارضه یابی شما با موفقیت ثبت شد.")

        return redirect(reverse("diagnose:form"))


class DownloadFileView(View):
    def get(self, request, *args, **kwargs):
        file_path = 'assets/files/form.pdf'

        absolute_file_path = os.path.join(settings.BASE_DIR, file_path)

        response = FileResponse(open(absolute_file_path, 'rb'))

        response['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(file_path)

        return response
