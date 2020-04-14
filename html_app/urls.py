from django.urls import path

app_name = "html"

from .views import html_view, html_list_view, html_form_view, html_input_view, html_anchor_view, html_ul_view

urlpatterns = [
    path('', html_view, name='html-homepage'),
    path('list/', html_list_view, name="html-list"),
    path('form/', html_form_view, name="html-form"),
    path('input/', html_input_view, name="html-input"),
    path('ul/', html_ul_view, name="html-input"),
    path('anchor/', html_anchor_view, name="html-input"),

]
