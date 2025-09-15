from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, DetailView, ListView
from rest_framework.generics import get_object_or_404

from restaurant.models import Page, Section, Table


# , DetailView, ListView)
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from blog.models import Article

# class MainMenuView(TemplateView):
#     template_name = 'restaurant/main_menu.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['pages'] = Page.objects.prefetch_related('page_sections').all()
#         return context


class SectionDetailView(DetailView):
    model = Section
    context_object_name = 'section'

    TEMPLATE_MAP = {
        "О ресторане": "restaurant/main_description.html",
        "Команда": "restaurant/about_team.html",
        "Услуги": "restaurant/main_services.html",
        "История ресторана": "restaurant/about_history.html",
        "Миссия и ценности": "restaurant/about_mission.html",
        "Контактная информация": "restaurant/main_contacts.html",
        "Обратная связь": "restaurant/main_feedback.html",
        "На главную": "restaurant/welcome.html",
        # "Управление бронированием": "users/profile.html",
        # "Выйти": "users/logout.html",
        # "Войти": "users/login.html",
        # "Зарегистрироваться": "users/register.html",
        # "Забронировать": "restaurant/book.html",
        # "Просмотр столиков": "restaurant/tables_list.html",
        #

    }

    def get_template_names(self):
        section = self.get_object()
        return [f'{self.TEMPLATE_MAP.get(section.name)}']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = Page.objects.all()
        context['user'] = self.request.user

        return context


# class HomePageView(DetailView):
#     model = Section
#     template_name = 'restaurant/welcome.html'
#
#
# class MainDescriptionView(DetailView):
#     model = Section
#     template_name = 'restaurant/main_description.html'
#     context_object_name = 'section'
#
#
# class MainServicesView(DetailView):
#     model = Section
#     template_name = 'restaurant/main_services.html'
#
#
# class MainContactsView(DetailView):
#     model = Section
#     template_name = 'restaurant/main_contacts.html'
#
#
# class MainFeedbackView(TemplateView):
#     model = Section
#     template_name = 'restaurant/main_feedback.html'
#
#
# class AboutHistoryView(DetailView):
#     model = Section
#     template_name = 'restaurant/about_history.html'
#
#
# class AboutMissionView(DetailView):
#     model = Section
#     template_name = 'restaurant/about_mission.html'
#
#
# class AboutTeamView(DetailView):
#     model = Section
#     template_name = 'restaurant/about_team.html'



# class SectionsByPagestView(ListView):
#     model = Product
#     template_name = 'catalog/products_by_category_list.html'
#
#     def get_queryset(self):
#         category_id = self.kwargs.get('pk')
#         return ProductService.get_products_by_category_cached(category_id)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category'] = get_object_or_404(Category, id=self.kwargs.get('pk'))
#         context['categories'] = Category.objects.all()
#         return context

#
# class ArticleDetailView(DetailView):
#     model = Article
#
#     def get_object(self, queryset=None):
#         obj = super().get_object(queryset)
#         obj.views += 1
#         obj.save()
#         return obj
#
#
# class ArticlesListView(ListView):
#     model = Article
#
#     def get_queryset(self):
#         return Article.objects.filter(is_published=True)
#
#
# class ArticleCreateView(CreateView):
#     model = Article
#     fields = ['title', 'content', 'preview']
#     success_url = reverse_lazy('blog:article_list')
#
#
# class ArticleUpdateView(UpdateView):
#     model = Article
#     fields = ['title', 'content', 'preview']
#
#     def get_success_url(self, **kwargs):
#         return reverse_lazy('blog:article_detail', kwargs={'pk': self.object.pk})
#
#
# class ArticleDeleteView(DeleteView):
#     model = Article
#     success_url = reverse_lazy('blog:article_list')