
from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('register/',views.register,name='register'),

    path('dashboard/',views.dashboard,name='dashboard'),

    path('projects/', views.project_list, name='project_list'),

    path('create-project/',views.create_project,name='create_project'),

    path('project/<int:id>/',views.project_detail,name='project_detail'),

    path('project/<int:id>/edit/',views.update_project,name='update_project'),

    path('project/<int:id>/delete/',views.delete_project,name='delete_project'),

    path('project/<int:project_id>/add-task/',views.create_task,name='create_task'),

    path('task/<int:id>/edit/',views.update_task,name='update_task'),

    path('task/<int:id>/delete/',views.delete_task,name='delete_task'),

    path('logout/',views.logout_user,name='logout'),

]

