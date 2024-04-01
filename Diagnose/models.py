from django.core.validators import FileExtensionValidator
from django.db import models
from django_jalali.db.models import jDateTimeField

from Home.validators import max_size_validator


class Diagnose(models.Model):
    user = models.ForeignKey(to="Account.CustomUser", on_delete=models.CASCADE, verbose_name="کاربر",
                             related_name="diagnoses")

    file = models.FileField(upload_to="Diagnoses/Diagnose/files", verbose_name="فایل",
                            validators=[FileExtensionValidator(["pdf"])])

    uploaded_at = jDateTimeField(verbose_name="آپلود شده در تاریخ", auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        db_table = "diagnose__diagnose"
        verbose_name = "عارضه یابی"
        verbose_name_plural = "عارضه یابی‌ها"
