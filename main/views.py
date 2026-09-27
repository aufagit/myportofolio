from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render,redirect
from main.models import Experience, Education
from main.forms import EducationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import datetime
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied  


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Aufa Nurcahyo",
        "npm": "2506656500",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "I'm Aufa, a Computer Science undergraduate at the University of Indonesia. "
            "Currently developing my skills in Python and HTML and have a strong foundation in Mathematics. "
            "I am highly interested in the field of Cybersecurity and also have a fundamental understanding of computer hardware. "
            "With a strong curiosity and commitment to continuous learning, I am eager to deepen my knowledge, "
            "gain practical experience, and contribute to projects in the areas of programming, cybersecurity, and technology development."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Aufa Nurcahyo",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    json_response = get_education_json(request)

    educations = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    education_list = [edu.object for edu in educations]
    institution_query = request.GET.get("institution", "").strip()

    context = {
        "name": "Aufa Nurcahyo",
        "education_list": education_list,
        "institution_query": institution_query,
    }
    return render(request, "education.html", context)

@login_required(login_url="/login/")
def create_education(request):

    if not request.user.is_superuser:
        raise PermissionDenied
    
    form = EducationForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")
        
    context = {
        "name": "Aufa Nurcahyo",
        "form": form,
    }
    return render(request, "education_form.html", context)

def get_education_json(request):
    institution_query = request.GET.get("institution", "").strip()
    educations = Education.objects.all()
    
    if institution_query:
        educations = educations.filter(institution__icontains=institution_query)
        
    educations_json = serializers.serialize(
        "json", educations, use_natural_foreign_keys=True)
    return HttpResponse(educations_json, content_type="application/json")

@login_required(login_url="/login/")
def delete_education(request, education_id):

    if not request.user.is_superuser:
        raise PermissionDenied
    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")
        return redirect("main:show_education")
    return redirect("main:show_education")

def edit_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    form = EducationForm(request.POST or None, instance=education)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_education')
        
    context = {
        'form': form,
        'name': 'Aufa Nurcahyo',
        'is_edit': True,
    }
    return render(request, 'education_form.html', context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Aufa Nurcahyo",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

# Tanpa cek is_superuser: semua akun yang sudah login boleh memberi star
@login_required(login_url="/login/")
def toggle_star(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in education.starred_by.all():
            education.starred_by.remove(request.user)
        else:
            education.starred_by.add(request.user)

    return redirect("main:show_projects")