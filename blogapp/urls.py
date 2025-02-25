from django.urls import path
from . import views
from .views import PostListView

app_name = "blogapp"

urlpatterns = [
    path('', views.PostListView.as_view(), name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:slug>/",
         views.post_detail,
         name="post_detail")
]
