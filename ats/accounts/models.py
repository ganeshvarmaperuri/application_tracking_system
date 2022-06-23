from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from PIL import Image
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE = (
        ('Recruiter', 'Recruiter'),
        ('Team Leader', 'Team Leader'),
        ('Hr Manager', 'Hr Manager'),
        ('Account Manager', 'Account Manager'),
        ('Director', 'Director'),
        ('Admin', 'Admin'),
    )
    email = models.EmailField(_('Email ID'), max_length=254, unique=True)
    employee_id = models.CharField(_('Employee ID'), max_length=20, null=True, blank=False)
    first_name = models.CharField(_('First name'), max_length=150, null=True, blank=False)
    last_name = models.CharField(_('Last Name'), max_length=150, null=True, blank=False)
    contact = models.CharField(_('Contact'), max_length=150, null=True, blank=False)
    designation = models.CharField(_('Designation'), max_length=150, null=True, blank=False)
    date_of_birth = models.DateField(_('Date of Birth'), null=True, blank=False)
    avatar = models.ImageField(_('Profile Picture'), default='profile_pic.png', upload_to='profile_pics', null=True,
                               blank=True)
    user_type = models.CharField(_('User Type'), choices=USER_TYPE, max_length=20)
    is_staff = models.BooleanField(_('Staff Status'), default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(_('Active'), default=True)
    last_login = models.DateTimeField(_('Last Login'), null=True, blank=True)
    date_joined = models.DateTimeField(_('Date Joined'), auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_email(self):
        return self.email

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)
