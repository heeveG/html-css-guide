from django.urls import path

app_name = "css"

from .views import css_view, css_list_view,css_flexbox_view, css_grid_view

urlpatterns = [
    path('', css_view, name='css-homepage'),
    path('list/', css_list_view, name='css-list'),
    path('flexbox/', css_flexbox_view, name='css-list'),
    path('grid/', css_grid_view, name='css-list'),
]
