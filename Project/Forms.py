from django import forms
# import User
from django.contrib.auth.models import User
# import the UserProfileInfo model
from Project.models import UserProfileInfo
# define a class that represents the SignUp for User built model
class UserForm(forms.ModelForm):
    # hide the password
    password = forms.CharField(widget=forms.PasswordInput())
    # define inner class Meta
    class Meta:
        # set the model
        model = User
        # set the fields to display in the form
        fields = ('username','password','email')
        # define a class that represents the SignUp for UserProfileInfo model
class UserProfileInfoForm(forms.ModelForm):
    # define inner class Meta
    class Meta:
        # set the model
        model = UserProfileInfo
        # set the fields to display in the form
        fields = ('phone',)