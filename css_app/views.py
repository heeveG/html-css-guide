from django.shortcuts import render


# Create your views here.

def css_view(request):
    return render(request, "css_app/css_homepage.html", {})


def css_list_view(request):
    return render(request, "css_app/css_list.html", {})

def css_flexbox_view(request):
    return render(request, "css_app/css_flexbox.html", {})

def css_grid_view(request):
    return render(request, "css_app/css_grid.html", {})