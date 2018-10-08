from django.urls import path
from . import views

app_name = 'QC'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:material_id>/', views.detail, name='detail'),
    path('<int:material_id>/process/', views.process, name='process'),
]
