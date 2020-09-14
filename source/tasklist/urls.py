"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from accounts.views import login_view, logout_view, RegisterView
from webapp.views import ProjectListView, ProjectCreate, Delete_Task, \
    ProjectView, Task_Update_View, Task_View, Task_Create, Delete_Project, Project_Update_View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProjectListView.as_view(), name='index'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/<int:pk>/update/', Project_Update_View.as_view(), name='update_project'),
    path('project/add/', ProjectCreate.as_view(), name='create'),
    path('project/<int:pk>/del/', Delete_Project.as_view(), name='del'),


    path('<int:pk>/edit/', Task_Update_View.as_view(), name='update'),
    path('project/task/<int:pk>',Task_View.as_view(), name='task'),
    path('project/<int:pk>/task/add/', Task_Create.as_view(), name='create_task'),
    path('<int:pk>/delet_task/', Delete_Task.as_view(), name='delete'),

    path('accounts/login', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('create/', RegisterView.as_view(), name='register')

]
