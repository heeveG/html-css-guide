from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.

def html_view(request):
    return render(request, "html_app/html_homepage.html", {})


def html_list_view(request):
    return render(request, "html_app/html_list.html")


def html_form_view(request):
    return render(request, "html_app/html_form.html")


def html_input_view(request):
    return render(request, "html_app/html_input.html")


def html_ul_view(request):
    return render(request, "html_app/html_ul.html")


def html_anchor_view(request):
    return render(request, "html_app/html_anchor.html")
