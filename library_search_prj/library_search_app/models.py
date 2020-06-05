from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
# Create your models here.
class UserManager(BaseUserManager):

	def create_user(self, username, password, last_name, email, phone, date_of_birth):
		user = self.model(
			username=username,
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

	def create_superuser(self, username, last_name, email, phone, date_of_birth, password):
		user = self.create_user(
			username=username,
			password=password,
			last_name=last_name,
			email=email,
			phone=phone,
			date_of_birth=date_of_birth
		)
		user.is_superuser=1
		user.is_staff=1
		user.save(using=self._db)
		return user
		
class User(AbstractBaseUser):
	password = models.CharField(max_length=128)
	username = models.CharField(unique=True, max_length=150)
	is_superuser = models.IntegerField()
	last_name = models.CharField(max_length=150)
	phone = models.CharField(max_length=20)
	email = models.CharField(max_length=254)
	date_of_birth = models.DateTimeField()
	date_joined = models.DateTimeField()
	last_login = models.DateTimeField(blank=True, null=True)
	is_staff = models.IntegerField(blank=True, null=True)
	is_active = models.IntegerField(blank=True, null=True)
	first_name = models.CharField(max_length=30, blank=True, null=True)

	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['last_name', 'phone', 'email', 'date_of_birth']

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

	class Meta:
		db_table = 'auth_user'