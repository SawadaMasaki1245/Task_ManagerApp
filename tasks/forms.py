from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']  # 入力できるフィールド
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),  # カレンダー入力
        }
