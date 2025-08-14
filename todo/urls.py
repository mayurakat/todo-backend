from django.urls import path
from rest_framework import routers
from .views import (
    TaskListCreateView,
    CategoryListView,
    ContextEntryListCreateView,
    AISuggestionsView,
    RegisterView, LoginView,LogoutView
)
router = routers.DefaultRouter()
router.register(r'tasks', TaskListCreateView, basename='task')          

urlpatterns = router.urls

urlpatterns += [
    # path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('contexts/', ContextEntryListCreateView.as_view(), name='context-list-create'),
    path('ai-suggestions/', AISuggestionsView.as_view(), name='ai-suggestions'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]