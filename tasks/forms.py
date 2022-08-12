from socket import fromshare
from django import forms  

from .models import Task #molde do formulário

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description')