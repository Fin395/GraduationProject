from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from booking.forms import ReservationForm
from booking.models import Reservation, Table
from config.settings import EMAIL_HOST_USER
from restaurant.models import Page


class TableListView(ListView):
    model = Table
    template_name = "booking/table_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pages"] = Page.objects.all()
        context["user"] = self.request.user
        context["tables"] = Table.objects.all()

        return context


class ReservationCreateView(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "booking/reservation_form.html"

    def get_success_url(self, **kwargs):
        return reverse_lazy("booking:reservation_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        reservation = form.save()
        user = self.request.user
        reservation.owner = user
        reservation.save()
        send_mail(
            subject="Rest-or-run. Бронирование",
            message=f"Уважаемый {user}! Спасибо, что выбрали наш ресторан! Ваша бронь подтверждена, ждем Вас"
            f" {reservation.date} в {reservation.time}!",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pages"] = Page.objects.all()
        context["image_path"] = "/static/images/image-22-09-25-07-08.jpg"

        # context['user'] = self.request.user
        # context['tables'] = Table.objects.all()
        return context


class ReservationUpdateView(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = "booking/reservation_form.html"

    def get_success_url(self, **kwargs):
        return reverse_lazy("booking:reservation_detail", kwargs={"pk": self.object.pk})

    def get_object(self, queryset=None):
        reservation = super().get_object(queryset)
        user = self.request.user
        if reservation.owner != user:
            raise PermissionDenied
        return reservation

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pages"] = Page.objects.all()
        context["user"] = self.request.user
        context["image_path"] = "/static/images/table.jpg"

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class ReservationDetailView(LoginRequiredMixin, DetailView):
    model = Reservation
    template_name = "booking/reservation_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pages"] = Page.objects.all()
        context["user"] = self.request.user
        context["tables"] = Table.objects.all()

        return context

    def get_queryset(self):
        return Reservation.objects.filter(owner=self.request.user)


class ReservationsToManageListView(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = "booking/current_reservations.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pages"] = Page.objects.all()
        context["user"] = self.request.user

        return context

    def get_queryset(self):
        return Reservation.objects.filter(owner=self.request.user, status="Открыта")


class ReservationsToHistoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Reservation
    template_name = "booking/reservation_history.html"
    permission_required = 'users.can_block_user'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pages"] = Page.objects.all()
        context["user"] = self.request.user

        return context

    def get_queryset(self):
        user = self.request.user
        if not user.has_perm('users.can_block_user'):
            return Reservation.objects.filter(owner=self.request.user)
        else:
            return Reservation.objects.all()




class ReservationCancelView(LoginRequiredMixin, View):
    def post(self, request, pk):
        reservation = get_object_or_404(Reservation, pk=pk)
        reservation.status = "Отменена"
        reservation.save()
        return redirect("booking:manage_reservations")
