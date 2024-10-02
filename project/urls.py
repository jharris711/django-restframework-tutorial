from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.api_root),
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
