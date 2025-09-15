from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from booking.forms import ReservationForm
from booking.models import Table, Reservation
from restaurant.models import Page


class TableListView(ListView):
    model = Table
    template_name = 'booking/table_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        context['user'] = self.request.user
        context['tables'] = Table.objects.all()

        return context


class ReservationCreateView(LoginRequiredMixin, CreateView):
        model = Reservation
        form_class = ReservationForm
        template_name = 'booking/reservation_form.html'
        # login_url = reverse_lazy('users:login')
        # permission_required = 'mailings.add_mailingrecipient'

        def get_success_url(self, **kwargs):
            return reverse_lazy('booking:table_list')
                                # kwargs={'pk': self.object.pk})

        def form_valid(self, form):
            reservation = form.save()
            user = self.request.user
            reservation.client = user
            reservation.save()
            return super().form_valid(form)

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['pages'] = Page.objects.all()
            context['image_path'] = '/static/images/table.jpg'

            # context['user'] = self.request.user
            # context['tables'] = Table.objects.all()
            return context

    # login_url = reverse_lazy('users:login')
    # permission_required = 'mailings.view_emailmessage'

    # def get_queryset(self):
    #     if not self.request.user.has_perm('mailings.can_cancel_mailing') and not self.request.user.has_perm(
    #             'users.can_block_user'):
    #         return EmailMessage.objects.filter(owner=self.request.user)
    #     return EmailMessage.objects.all()