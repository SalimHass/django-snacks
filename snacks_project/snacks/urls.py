from django.urls import path
from .views import (
                        HomeView, 
                        AboutView,
                        SnackListView
                    )


urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('about',AboutView.as_view(), name='about'),
    path('snack-list',SnackListView.as_view(), name='snack_list'),
]