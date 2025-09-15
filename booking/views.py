from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from booking.models import Table
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
    # login_url = reverse_lazy('users:login')
    # permission_required = 'mailings.view_emailmessage'

    # def get_queryset(self):
    #     if not self.request.user.has_perm('mailings.can_cancel_mailing') and not self.request.user.has_perm(
    #             'users.can_block_user'):
    #         return EmailMessage.objects.filter(owner=self.request.user)
    #     return EmailMessage.objects.all()