from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name= 'home'),
    path('mcq/',views.mcq,name='mcq'),
    path('subjects_maths',views.maths,name='subjects_maths'),
    path('subjects_bee',views.bee,name='subjects_bee'),
    path('subjects_mechanics',views.mechanics,name='subjects_mechanics'),
    path('subjects_physics',views.physics,name='subjects_physics'),
    path('subjects_chemistry',views.chemistry,name='subjects_chemistry'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('feedback',views.feedback,name='feedback')
]