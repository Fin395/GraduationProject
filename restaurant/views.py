from django.views.generic import DetailView

from restaurant.models import Page, Section


class SectionDetailView(DetailView):
    model = Section
    context_object_name = "section"

    TEMPLATE_MAP = {
        "О нас": "restaurant/main_description.html",
        "Команда": "restaurant/about_team.html",
        "Услуги": "restaurant/main_services.html",
        "История ресторана": "restaurant/about_history.html",
        "Миссия и ценности": "restaurant/about_mission.html",
        "Контактная информация": "restaurant/main_contacts.html",
        "Обратная связь": "restaurant/main_feedback.html",
        "На главную": "restaurant/welcome.html",
    }

    def get_template_names(self):
        section = self.get_object()
        return [f"{self.TEMPLATE_MAP.get(section.name)}"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pages"] = Page.objects.all()
        context["user"] = self.request.user

        return context


#     def get_queryset(self):
#         category_id = self.kwargs.get('pk')
#         return ProductService.get_products_by_category_cached(category_id)
#
#

#
#     def get_success_url(self, **kwargs):
#         return reverse_lazy('blog:article_detail', kwargs={'pk': self.object.pk})
