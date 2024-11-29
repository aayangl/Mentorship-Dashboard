from django import forms
from .models import Student, Mentor

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'college', 'course', 'year_of_study', 'interests']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'college': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your college name'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your course'}),
            'year_of_study': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your year of study'}),
            'interests': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your interests and goals', 'rows': 4}),
        }

class MentorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['name', 'email', 'phone', 'company', 'designation', 'experience_years', 'expertise']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your company name'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your designation'}),
            'experience_years': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Years of experience'}),
            'expertise': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your areas of expertise', 'rows': 4}),
        }
