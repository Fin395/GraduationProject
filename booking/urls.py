from django.urls import path

from booking.apps import BookingConfig
from booking.views import (ReservationCancelView, ReservationCreateView,
                           ReservationDetailView,
                           ReservationsToHistoryListView,
                           ReservationsToManageListView, ReservationUpdateView,
                           TableListView)

app_name = BookingConfig.name

urlpatterns = [
    path("tables/", TableListView.as_view(), name="table_list"),
    path("reservation/", ReservationCreateView.as_view(), name="reservation_create"),
    path(
        "<int:pk>/reservation/update/",
        ReservationUpdateView.as_view(),
        name="reservation_update",
    ),
    path(
        "manage_reservations/",
        ReservationsToManageListView.as_view(),
        name="manage_reservations",
    ),
    path(
        "reservations_history/",
        ReservationsToHistoryListView.as_view(),
        name="reservation_history",
    ),
    path("<int:pk>/", ReservationDetailView.as_view(), name="reservation_detail"),
    path(
        "<int:pk>/reservation/cancel/",
        ReservationCancelView.as_view(),
        name="reservation_cancel",
    ),
]
