from django import forms
from .models import ToDoItem

class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['title', 'description', 'status', 'due_date']
    
    due_date=forms.DateField(widget = forms.SelectDateWidget())

