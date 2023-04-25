from django.urls import path
from simpleapp.views import NewList, NewDetailView, NewCreateView, NewUpdateView, NewDeleteView

urlpatterns = [
    path('', NewList.as_view()),
    path('<int:pk>/', NewDetailView.as_view(), name='new_detail'),
    path('create/', NewCreateView.as_view(), name='new_create'),
    path('<int:pk>/create/', NewUpdateView.as_view(), name='new_update'),
    path('<int:pk>/delete/', NewDeleteView.as_view(), name='new_delete'),
]














