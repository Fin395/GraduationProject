from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from booking.models import Table


class TableListView(LoginRequiredMixin, ListView):
    model = Table
    template_name = 'restaurant/table_list.html'
    # login_url = reverse_lazy('users:login')
    # permission_required = 'mailings.view_emailmessage'

    # def get_queryset(self):
    #     if not self.request.user.has_perm('mailings.can_cancel_mailing') and not self.request.user.has_perm(
    #             'users.can_block_user'):
    #         return EmailMessage.objects.filter(owner=self.request.user)
    #     return EmailMessage.objects.all()