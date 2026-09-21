from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render,redirect
from main.models import Experience, Education
from main.forms import EducationForm


def show_main(request):
    context = {
        "name": "Aufa Nurcahyo",
        "npm": "2506656500",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "I'm Aufa, , a Computer Science undergraduate at the University of Indonesia. Currently developing my skills in Python and HTML and have a strong foundation in Mathematics. I am highly interested in the field of Cybersecurity and also have a fundamental understanding of computer hardware. With a strong curiosity and commitment to continuous learning, I am eager to deepen my knowledge, gain practical experience, and contribute to projects in the areas of programming, cybersecurity, and technology development."
        ),
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

def create_education(request):
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
        
    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")

def delete_education(request, education_id):
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