from django.urls import path
from news_app import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('newsadd/', views.newsadd),
    path('authoradd/', views.authoradd),
    path('author/<int:id>/', views.author_detail)
]



