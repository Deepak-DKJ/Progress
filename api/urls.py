from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('list/', views.ChapterItemList.as_view()),
    path('create/', views.ChapterItemCreate.as_view()),
    path('update/<int:id>', views.ChapterItemUpdate.as_view()),
    path('delete/<int:id>', views.ChapterItemDestroy.as_view()),
]
