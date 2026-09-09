from django.shortcuts import render

from main.models import Experience


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
        "name": "Aufa",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)