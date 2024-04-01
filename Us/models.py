from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django_jalali.db.models import jDateTimeField

from Account.models import CustomUser


class Message(models.Model):
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, related_name='messages', blank=True, null=True)

    mobile_phone = models.CharField(max_length=11, blank=True, null=True)

    email = models.EmailField(max_length=254, blank=True, null=True)

    full_name = models.CharField(max_length=100, blank=True, null=True)

    message = CKEditor5Field(config_name='extends')

    created_at = jDateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f"{self.user.username}"

        else:
            sender_name = ", ".join(filter(None, [self.full_name, self.mobile_phone, self.email]))
            return f"{sender_name}" if sender_name else "ناشناس"

    class Meta:
        db_table = 'us__message'
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام‌ها'


class SocialMedia(models.Model):
    phone_1 = models.CharField(max_length=11, blank=True, null=True, verbose_name='شماره تلفن اول')

    phone_2 = models.CharField(max_length=11, blank=True, null=True, verbose_name='شماره تلفن دوم')

    telegram_url = models.URLField(blank=True, null=True, verbose_name='لینک تلگرام')

    telegram_icon = models.ImageField(upload_to="Us/SocialMedia/icons", blank=True, null=True,
                                      verbose_name='آیکون تلگرام')

    telegram_number = models.CharField(max_length=13, blank=True, null=True, verbose_name='شماره تلگرام')

    whats_App_url = models.URLField(blank=True, null=True, verbose_name='لینک واتس‌اپ')

    whats_App_icon = models.ImageField(upload_to="Us/SocialMedia/icons", blank=True, null=True,
                                       verbose_name='آیکون واتس‌اپ')

    whats_App_number = models.CharField(max_length=13, blank=True, null=True, verbose_name='شماره واتس اپ')

    linkedIn_url = models.URLField(blank=True, null=True, verbose_name='لینک لینکدین')

    linkedIn_icon = models.ImageField(upload_to="Us/SocialMedia/icons", blank=True, null=True,
                                      verbose_name='آیکون لینکدین')

    pinterest_url = models.URLField(blank=True, null=True, verbose_name='لینک پینترست')

    pinterest_icon = models.ImageField(upload_to="Us/SocialMedia/icons", blank=True, null=True,
                                       verbose_name='آیکون پینترست')

    instagram_url = models.URLField(blank=True, null=True, verbose_name='لینک اینستاگرام')

    instagram_icon = models.ImageField(upload_to="Us/SocialMedia/icons", blank=True, null=True,
                                       verbose_name='آیکون اینستاگرام')

    twitter_url = models.URLField(blank=True, null=True, verbose_name='لینک توییتر')

    twitter_icon = models.ImageField(upload_to="Us/SocialMedia/icons", blank=True, null=True,
                                     verbose_name='آیکون توییتر')

    facebook_url = models.URLField(blank=True, null=True, verbose_name='لینک فیس‌بوک')

    facebook_icon = models.ImageField(upload_to="Us/SocialMedia/icons", blank=True, null=True,
                                      verbose_name='آیکون فیس‌بوک')

    def __str__(self):
        return f"شبکه اجتماعی"

    class Meta:
        db_table = 'us__social_media'
        verbose_name = 'شبکه اجتماعی'
        verbose_name_plural = 'شبکه‌های اجتماعی'


class AboutUs(models.Model):
    name = models.CharField(max_length=75, verbose_name='نام')

    short_description = CKEditor5Field(config_name="extends", verbose_name="توضیح مختصر")

    what_we_do = CKEditor5Field(config_name="extends", verbose_name="چی کار می‌کنیم")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'us__about_us'
        verbose_name = 'درباره'
        verbose_name_plural = 'درباره ما'


class TeamMember(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام')

    role = models.CharField(max_length=100, verbose_name='نقش')

    about = models.TextField(max_length=250, verbose_name='درباره')

    image = models.ImageField(upload_to="Us/TeamMembers/images")

    def __str__(self):
        return f"{self.name}"


class WhatDoCustomersEarn(models.Model):
    title = models.CharField(max_length=100, verbose_name='تیتر')

    description = models.TextField(max_length=250, verbose_name='توضیحات')

    icon = models.ImageField(upload_to="Us/WhatDoCustomersEarns/icons", verbose_name="آیکون")

    class Meta:
        db_table = 'us__what_do_customers_earn'
        verbose_name = 'مشتریان چه نتیجه‌ای دریافت می‌کنند؟'
        verbose_name_plural = 'مشتریان چه نتایجی را دریافت می‌کنند؟'


class Service(models.Model):
    pass


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام شرکت')

    link = models.URLField(blank=True, null=True, verbose_name='آدرس سایت')

    description = CKEditor5Field(config_name='extends', verbose_name='توضیحات')

    icon = models.ImageField(upload_to="Us/Customer/icons", blank=True, null=True)

    image = models.ImageField(upload_to="Us/Customer/images", blank=True, null=True)

    slug = models.SlugField(allow_unicode=True, max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'us__customer'
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'
