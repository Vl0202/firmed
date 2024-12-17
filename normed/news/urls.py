from django.urls import path

from . import views


app_name = 'news'

urlpatterns = [
    path('<int:pk>/', views.news_detail, name='news_detail'),
     path('category/<slug:category_slug>/',
         views.category_news, name='category_news'),
    path('create/', views.NewCreateView.as_view(), name='create_new'),
    path('<int:pk>/edit/', views.NewUpdateView.as_view(), name='edit_new'),
    path('<int:pk>/delete/', views.NewDeleteView.as_view(), name='delete_new'),
    path('<int:pk>/comment/', views.add_comment, name='add_comment'),
    path('<int:new_id>/edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('<int:new_id>/delete_comment/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),
    path('', views.news_list, name='news_list')
]
