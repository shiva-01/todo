from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import settings
from todoapp import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todoapp/', include('todoapp.urls')),

    url(r'^$',app_views.login_view, name="login"),
    url(r'^signup/$', app_views.signup, name="signup"),
    url(r'^logout/$', app_views.logout_view, name="logout"),

    url(r'^todo/$', app_views.todoList, name="todoList"),
    url(r'^deleteTask/(?P<task_id>\d+)/$', app_views.deleteTask, name="deleteTask"),
    url(r'^task_compleated/(?P<task_id>\d+)/$', app_views.task_compleated, name="task_compleated"),
    url(r'^task_not_compleated/(?P<task_id>\d+)/$', app_views.task_not_compleated, name="task_not_compleated"),
    url(r'^editTask/(?P<task_id>\d+)/$', app_views.editTask, name="editTask"),
]
