from django.urls import path
from . import views

app_name="dashboard"

urlpatterns = [
    path('dashboard/', views.dashboardBlog, name="dashboard"),
    path('newblog/', views.newBlog, name="newblog"),
    path('update/<int:pk>/', views.updateBlog, name="updateblog"),
    path('delete/<int:pk>/', views.deleteBlog, name="deleteblog"),
]