from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

#CustomUser model is imported via get_user_model

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model=get_user_model()
        fields=('email', 'username')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=get_user_model()
        fields=('email', 'username')
