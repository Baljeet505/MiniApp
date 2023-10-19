from django.db import models

# Create your models here.
from django.contrib.auth.models import User
####################################
# create a model that represents your User
# inherit this class from the built in models.Model
class UserProfileInfo (models.Model):
    # declare a foreign key object of the User
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=models.DO_NOTHING)
    # define additional features
    phone = models.CharField(max_length=255)
    def __str__(self):
        return self.user.username