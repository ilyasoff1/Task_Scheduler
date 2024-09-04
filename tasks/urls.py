from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
	path('list/', views.task_list),# name='task-list'),
	path('detail/<int:pk>', views.task_detail), #name='task-detail'),
	path('update/<int:pk>', views.task_update), #name='task-update'),
	path('create/', views.task_create), #name='task-create'),
	path('delete/<int:pk>', views.task_delete), #name='task-delete'), 
]
