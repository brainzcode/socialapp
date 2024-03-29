from django.forms import ModelForm
from .models import Room, Message, User
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['profile_pic', 'first_name', 'last_name', 'username', 'email', 'bio']