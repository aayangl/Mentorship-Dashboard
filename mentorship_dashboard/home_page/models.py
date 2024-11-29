from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    college = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    year_of_study = models.IntegerField()
    interests = models.TextField()
    academic_challenges = models.TextField(blank=True, null=True)  # New field
    preferred_mentorship_format = models.TextField(blank=True, null=True)  # New field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Mentor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    company = models.CharField(max_length=200)
    designation = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    expertise = models.TextField()
    qualification = models.CharField(max_length=200, default='Not Specified')  # Existing field
    preferred_mentorship_format = models.TextField(blank=True, null=True)  # New field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
