from uuid import uuid4

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django_jalali.db.models import jDateTimeField


class CustomUserManager(BaseUserManager):
    def create_user(self, mobile_phone, email=None, password=None, **extra_fields):
        if not mobile_phone:
            raise ValueError("شماره تلفن الزامی است.")

        user = self.model(mobile_phone=self.normalize_phone(mobile_phone),
                          email=self.normalize_email(email) if email else None, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("None")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("None")

        return self.create_user(mobile_phone, email, password, **extra_fields)

    def normalize_phone(self, mobile_phone):
        return ''.join(filter(str.isdigit, mobile_phone))


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=75, unique=True, verbose_name='نام کاربری')

    slug = models.SlugField(unique=True, verbose_name='اسلاگ', blank=True, null=True)

    mobile_phone = models.CharField(max_length=11, unique=True, verbose_name='شماره تلفن')

    email = models.EmailField(max_length=254, unique=True, blank=True, null=True,
                              verbose_name='آدرس ایمیل')

    full_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")

    image = models.ImageField(upload_to='Account/Users/profiles/', verbose_name="تصویر پروفایل", blank=True, null=True)

    company_name = models.CharField(max_length=100, verbose_name="نام شرکت")

    about = models.TextField(verbose_name="درباره", blank=True, null=True)

    is_staff = models.BooleanField(default=False, verbose_name='آیا کارمند است؟')

    is_active = models.BooleanField(default=True, verbose_name="آیا فعال است؟")

    date_joined = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ پیوستن')

    USERNAME_FIELD = 'mobile_phone'

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"


class OTP(models.Model):
    otp_type_choices = (
        ("R", "ثبت نام"),
        ("F", "فراموشی رمز عبور"),
        ("D", "حذف حساب کاربری"),
    )

    username = models.CharField(max_length=75, blank=True, null=True, verbose_name='نام کاربری')

    slug = models.SlugField(blank=True, null=True, verbose_name='اسلاگ')

    mobile_phone = models.CharField(max_length=11, verbose_name='شمارع تلفن')

    password = models.CharField(max_length=100, verbose_name='رمز عبور', editable=False)

    full_name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")

    company_name = models.CharField(max_length=100, verbose_name="نام شرکت")

    sms_code = models.CharField(max_length=4, verbose_name='کد تایید')

    uuid = models.UUIDField(editable=False)

    authentication_token = models.UUIDField(blank=True, null=True, verbose_name="یو یو آی دی")

    otp_type = models.CharField(max_length=1, choices=otp_type_choices)

    class Meta:
        verbose_name = "رمز یکبار مصرف"
        verbose_name_plural = "رمزهای یکبار مصرف"

    def __str__(self):
        return f"{self.mobile_phone}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super().save(*args, **kwargs)


class Notification(models.Model):
    """
    A model for managing user notifications within the application.

    This model provides a flexible and robust framework for creating different
    types of notifications (safe, caution, danger), targeting specific
    user groups (global or private), and offering rich text formatting capabilities
    through the CKEditor5Field.

    Fields:
        title (CharField): A concise and informative notification title.
        message (CKEditor5Field): The notification's detailed content, supporting
        rich text formatting for enhanced user experience.
        users (ManyToManyField): A relationship to link notifications with
        specific CustomUser instances (blank=True allows for global notifications).
        created_at (jDateTimeField): An automatically populated field recording
        the notification's creation timestamp.
        mode (CharField): The notification's severity level (choices from mode_choices).
        visibility (CharField): The notification's target audience (choices from visibility_choices).
    """

    mode_choices = (
        ("S", "Safe"),
        ("C", "Caution"),
        ("D", "Danger"),
    )

    visibility_choices = (
        ("G", "Global"),
        ("P", "Private"),
    )

    uuid = models.UUIDField(default=uuid4, editable=False)

    title = models.CharField(max_length=100)

    message = CKEditor5Field(config_name='extends')

    image = models.ImageField(upload_to="Account/Notification/image", blank=True, null=True)

    users = models.ManyToManyField(to=CustomUser, blank=True)

    created_at = jDateTimeField(auto_now_add=True)

    mode = models.CharField(max_length=1, choices=mode_choices)

    visibility = models.CharField(max_length=1, choices=visibility_choices)

    has_been_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'account__notification'
        verbose_name = "اعلانیه"
        verbose_name_plural = "اعلانیه‌ها"
