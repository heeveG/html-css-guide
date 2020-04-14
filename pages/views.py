from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):  # *args, **kwargs
    return render(request, "base.html", {})


def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})


def references_view(request, *args, **kwargs):
    return render(request, "references.html", {})
