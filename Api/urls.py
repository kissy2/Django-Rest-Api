from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiEntrypoints, name="api-entrypoints"),
	path('list/', views.NoteList, name="list"),
	path('get/<str:pk>/', views.NoteDetail, name="detail"),
	path('create/', views.NoteCreate, name="create"),
	path('update/<str:pk>/', views.NoteUpdate, name="update"),
	path('delete/<str:pk>/', views.NoteDelete, name="delete"),
]
