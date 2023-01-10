from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	"""Model definition for UserProfile."""

	user = models.OneToOneField(User,on_delete=models.CASCADE)

	class Meta:
		"""Meta definition for UserProfile."""

		verbose_name = 'UserProfile'
		verbose_name_plural = 'UserProfiles'

	def __str__(self):
		"""Unicode representation of UserProfile."""
		self.name


	def get_absolute_url(self):
		"""Return absolute url for UserProfile."""
		return ('user-profile',{'pk':self.pk})

	# TODO: Define custom methods here
