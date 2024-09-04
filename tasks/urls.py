from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
	path('list/', views.task_list),
	path('detail/<int:pk>', views.task_detail),
	path('update/<int:pk>', views.task_update),
	path('create/', views.task_create),
	path('delete/<int:pk>', views.task_delete),
]
