from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    portfolio_link = models.URLField(blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    gpa = models.CharField(max_length=20, blank=True)
    coursework = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.degree} at {self.institution}"

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.role} at {self.company}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True, help_text="External image URL (optional)")
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('LANG', 'Languages'),
        ('FRAME', 'Frameworks / Web Technologies'),
        ('DB', 'Databases / Tools'),
        ('CONC', 'Core Concepts & Systems / Security'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.name

class Capability(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="FontAwesome class name (e.g., 'fas fa-code')")
    
    def __str__(self):
        return self.title

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Leadership(models.Model):
    role = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.role} at {self.organization}"
