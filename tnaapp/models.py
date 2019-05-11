# -*- coding: utf-8 -*-
from django.contrib.auth.models import (
    AbstractBaseUser
)
from django.db import models
from django.utils import timezone

BOARD_MEMBER_POST = (
    ('CM', 'CHAIRMAN'),
    ('VC', 'VICE-CHAIRMAN'),
    ('SE', 'SECRETARY'),
    ('TR', 'TREASURER'),
    ('DO', 'DevOps'),
)

MEMBER_TYPE = (
    ('BM', 'BOARD MEMBER'),
    ('ME', 'MEMBER'),
)


class Member(models.Model):
    token = models.CharField(max_length=60000, unique=True)
    password = models.CharField(max_length=60)
    post_type = models.CharField(max_length=2, choices=MEMBER_TYPE, default='ME')
    post = models.CharField(max_length=2, choices=BOARD_MEMBER_POST, null=True, blank=True)
    first_name = models.CharField(max_length=50, blank=True, null=True, default=' ')
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    address = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    url = models.URLField(max_length=100, blank=True, null=True)
    fb_url = models.URLField(blank=True, null=True)
    tw_url = models.URLField(blank=True, null=True)
    ln_url = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    google = models.URLField(blank=True, null=True)
    skype = models.CharField(max_length=120, blank=True, null=True)
    is_board_member = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    ev_token = models.CharField(max_length=100, null=True, blank=True)
    pr_token = models.CharField(max_length=100, null=True, blank=True)

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email.encode('utf8')

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a owner of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Info(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField()
    owner = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.title.encode('utf8'))

    class Meta:
        ordering = ['-date_posted']


class Events(models.Model):
    owner = models.ForeignKey(Member, related_name="events", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    reference_number = models.CharField(max_length=100, blank=True, null=True, default="")
    registration = models.BooleanField(default=False)
    adult_price = models.IntegerField(default=0)
    family_price = models.IntegerField(default=0)
    children_price = models.IntegerField(default=0)
    registration_open = models.BooleanField(default=False)
    datetime = models.DateTimeField()
    expiry_datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s" % (self.title.encode('utf8'))


class Gallery(models.Model):
    owner = models.ForeignKey(Member, related_name="gallery", on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return "%s" % (self.title.encode('utf8'))


def getMemberPath(instance, filename):
    return 'members/{0}/{1}'.format(instance.owner.id, filename)


class ProfilePictures(models.Model):
    owner = models.OneToOneField(Member, related_name="profile_pic", on_delete=models.CASCADE)
    url = models.ImageField(upload_to=getMemberPath)

    def __unicode__(self):
        return u"%d. Owner:[%s], URL: %s" % (self.id, self.owner, self.url.url)


def getGalleryPath(instance, filename):
    return 'gallery/{0}/{1}'.format(instance.gallery.id, filename)


class GalleryPictures(models.Model):
    gallery = models.ForeignKey(Gallery, related_name="content", on_delete=models.CASCADE)
    cover_photo = models.CharField(max_length=300, null=True, blank=True)
    url = models.ImageField(upload_to=getGalleryPath)

    def __unicode__(self):
        return u"%d. Owner:[%s], URL: %s" % (self.id, self.gallery, self.url.url)


def getHomePath(instance, filename):
    return 'home/{0}/{1}'.format(instance.owner.id, filename)


class HomePictures(models.Model):
    owner = models.ForeignKey(Member, related_name="homepictures", on_delete=models.CASCADE)
    url = models.ImageField(upload_to=getHomePath)

    def __unicode__(self):
        return u"%d. Owner:[%s], URL: %s" % (self.id, self.owner, self.url.url)


def getInfoPath(instance, filename):
    return 'info/{0}/{1}'.format(instance.info.id, filename)


class InfoPictures(models.Model):
    info = models.ForeignKey(Info, related_name="content", on_delete=models.CASCADE)
    url = models.ImageField(upload_to=getInfoPath)

    def __unicode__(self):
        return u"%d. Owner:[%s], URL: %s" % (self.id, self.info, self.url.url)


def getEventsPath(instance, filename):
    return 'events/{0}/{1}'.format(instance.events.id, filename)


class EventsPictures(models.Model):
    events = models.ForeignKey(Events, related_name="content", on_delete=models.CASCADE)
    url = models.ImageField(upload_to=getEventsPath)

    def __unicode__(self):
        return u"%d. Owner:[%s], URL: %s" % (self.id, self.events, self.url.url)


class EventAttendees(models.Model):
    events = models.ForeignKey(Events, related_name="attendees", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    no_adults = models.CharField(max_length=5, default=0)
    no_family = models.CharField(max_length=5, default=0)
    no_children = models.IntegerField(default=0)
    no_vegetarian = models.IntegerField(default=0)
    total = models.CharField(max_length=10, default=0)
    has_paid = models.BooleanField(default=False)
    email_reminder_sent = models.BooleanField(default=False)

    def __unicode__(self):
        return u"%d. Attendees:[%s]" %(self.id, self.name)

MONTH_NAME = (
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December'),
)


class AccountFile(models.Model):
    url = models.FileField(upload_to='accounts')

    def __unicode__(self):
        return u"%d." % (self.id)

class Account(models.Model):
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    beneficiary = models.CharField(max_length=200, blank=True, null=True)
    amount = models.CharField(max_length=10)
    ref_num = models.CharField(max_length=100)

    def __unicode__(self):
        return u"%d. %d-%d-%d %s %s" % (self.id, self.day, self.month, self.year, self.beneficiary, self.amount)

    class Meta:
        unique_together = ('year', 'month', 'day', 'beneficiary', 'amount', 'ref_num',)

