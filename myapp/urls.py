from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('APIViews/', views.NoteAPIView.as_view(), name='APIViews'),
    path('APIDetailViews/<int:id>/', views.NoteDetailAPIView.as_view(), name='APIDetailViews'),
    path('notes/', views.NoteListCreateAPIView.as_view(), name='notes'),
    path('notes/<int:pk>/', views.NoteRetrieveUpdateDestroyAPIView.as_view(), name='note-detail'),
    
]
