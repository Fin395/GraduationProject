from django.urls import path

from restaurant.apps import RestaurantConfig
from restaurant.views import SectionDetailView

app_name = RestaurantConfig.name

urlpatterns = [
    path("section/<int:pk>/", SectionDetailView.as_view(), name="section_detail"),
]
