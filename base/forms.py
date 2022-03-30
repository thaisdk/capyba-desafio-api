from django.forms import ModelForm
from .models import Article
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['author']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']