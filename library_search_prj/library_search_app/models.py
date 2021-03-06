from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from datetime import datetime
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, user_id, password, last_name, email, phone, date_of_birth):
        user = self.model(
            user_id=user_id,
            last_name=last_name,
            email=self.normalize_email(email),
            phone=phone,
            date_of_birth=date_of_birth,
            date_joined=timezone.now(),
            is_superuser=0,
            is_staff=0,
            is_active=1
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password, last_name, email, phone, date_of_birth):
        user = self.create_user(
            user_id=user_id,
            password=password,
            last_name=last_name,
            email=email,
            phone=phone,
            date_of_birth=timezone.now())
        user.is_superuser = 1
        user.is_staff = 1
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_id = models.CharField(unique=True, max_length=150)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=254)
    last_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    is_staff = models.IntegerField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['last_name', 'phone', 'email', 'date_of_birth']

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class BoardCategories(models.Model):
    # category_parents = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=100)
    list_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "%s" % self.category_name


class Boards(models.Model):
    category = models.ForeignKey(BoardCategories, models.DO_NOTHING)
    board_type = models.CharField(max_length=50)
    user = models.ForeignKey(User, models.DO_NOTHING)
    title = models.CharField(max_length=300)
    content = RichTextUploadingField(blank=True, null=True)
    registered_date = models.DateTimeField(default=timezone.now)
    last_update_date = models.DateTimeField(default=timezone.now)
    view_count = models.IntegerField(blank=True, default=0)


class BoardReplies(models.Model):
    article = models.ForeignKey(Boards, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    level = models.IntegerField(blank=True, null=True)
    content = models.TextField()
    registered_date = models.DateTimeField(default=timezone.now)
    last_update_date = models.DateTimeField(default=timezone.now)
    reference_reply_id = models.IntegerField(blank=True, null=True)


class BoardLikes(models.Model):
    article = models.ForeignKey(Boards, models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    registered_date = models.DateTimeField(default=timezone.now)
