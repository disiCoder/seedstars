from django.db import models

# Create your models here.
# Create your models here
class User(models.Model):
	email = models.EmailField(max_length=250)
	full_name = models.CharField(max_length=250, null=True, blank=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.full_name
	def list(self):
                return (self.full_name, email)
        def add(self, name, email):
