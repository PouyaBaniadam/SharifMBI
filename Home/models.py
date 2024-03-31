from django.db import models
from django_jalali.db.models import jDateTimeField


class HeroBanner(models.Model):
    title = models.CharField(max_length=1000)

    link = models.URLField(blank=True, null=True, unique=True)

    file = models.FileField(upload_to="Home/HeroBanner/file")

    can_be_shown = models.BooleanField(default=True)

    created_at = jDateTimeField(auto_now_add=True)

    updated_at = jDateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "هیرو بنر"
        verbose_name_plural = "هیرو بنرها"
        ordering = ('-created_at',)
