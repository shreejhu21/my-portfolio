from django.shortcuts import render
from .models import Profile, Education, Experience, Project, Skill, Capability, Certification, Leadership

def index(request):
    profile = Profile.objects.first()
    education = Education.objects.all().order_by('-end_date')
    experience = Experience.objects.all().order_by('-end_date')
    projects = Project.objects.all().order_by('-date')
    skills = Skill.objects.all()
    
    skills_by_category = {}
    for code, label in Skill.CATEGORY_CHOICES:
        skills_by_category[label] = skills.filter(category=code)

    capabilities = Capability.objects.all()
    certifications = Certification.objects.all().order_by('-date')
    leadership = Leadership.objects.all()
    
    context = {
        'profile': profile,
        'education': education,
        'experience': experience,
        'projects': projects,
        'skills_by_category': skills_by_category,
        'capabilities': capabilities,
        'certifications': certifications,
        'leadership': leadership,
    }
    return render(request, 'portfolio/index.html', context)
