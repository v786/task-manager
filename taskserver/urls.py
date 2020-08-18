from django.urls import path

from . import views

app_name = 'taskserver'
urlpatterns = [
    path('', views.get, name='index'),
    path('post/', views.post, name='create'),
    path('delete/<int:server_id>', views.delete, name='delete'),
    path('add_task/<int:server_id>', views.add_task, name='add_task'),
    # # ex: /candidates/5/
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # # ex: /candidates/5/results/
    # path('<int:pk>/results/', views.DetailView.as_view(), name='results'),
    # # ex: /candidates/5/vote/
    # path('<int:candidate_id>/vote/', views.vote, name='vote'),
]