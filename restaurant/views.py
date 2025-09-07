from django.views.generic import TemplateView, CreateView


# , DetailView, ListView)
# from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from blog.models import Article

class DescriptionView(TemplateView):
    template_name = 'restaurant/description.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_path'] = '/static/images/IMG-20250906-WA0030.jpg'

        return context


class ContactsView(TemplateView):
    template_name = 'restaurant/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_path'] = '/static/images/krasivyi-snimok-goroda-dinastii-sun-sihu-kitai.jpg'

        return context


class ServicesView(TemplateView):
    template_name = 'restaurant/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_path'] = '/static/images/IMG-20250906-WA0028 (3).jpg'

        return context


class FeedbackView(TemplateView):
    template_name = 'restaurant/feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_path'] = '/static/images/feedback.jpg'

        return context


class HistoryView(TemplateView):
    template_name = 'restaurant/history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_path'] = '/static/images/20250907_014507.jpg'

        return context


class MissionView(TemplateView):
    template_name = 'restaurant/mission.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_path'] = '/static/images/20230915_182702.jpg'

        return context


class TeamView(TemplateView):
    template_name = 'restaurant/team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_path'] = '/static/images/team.jpg'

        return context



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