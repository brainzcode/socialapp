from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Room, Message


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
        fields = ['username', 'email']