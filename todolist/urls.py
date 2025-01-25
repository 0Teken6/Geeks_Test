from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.TaskListAPIView.as_view()),
    path('create/', views.TaskCreateAPIView.as_view()),
    path('retrieve/<int:pk>/', views.TaskRetrieveAPIView.as_view()),
    path('update/<int:pk>/', views.TaskUpdateAPIView.as_view()),
    path('destroy/<int:pk>/', views.TaskDestroyAPIView.as_view()),
]