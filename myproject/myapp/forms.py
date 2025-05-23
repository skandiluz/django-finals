from django import forms
from django.forms import ModelForm
from .models import Student  # Import your model

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email']
        # You can also specify widgets, labels, help_text, etc.
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Full Name',
            'age': 'Age',
            'email': 'Email Address',
        }