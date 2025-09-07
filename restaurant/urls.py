from django.urls import path
from restaurant.apps import RestaurantConfig
from restaurant.views import DescriptionView, ContactsView, ServicesView, FeedbackView, HistoryView, MissionView, \
    TeamView

# , BlogContactsView, ArticleDetailView, ArticlesListView, ArticleCreateView, \
#     ArticleUpdateView, ArticleDeleteView)

app_name = RestaurantConfig.name

urlpatterns = [
    path('description/', DescriptionView.as_view(), name='description'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('services/', ServicesView.as_view(), name='services'),
    path('feedback/', FeedbackView.as_view(), name='feedback'),
    path('history/', HistoryView.as_view(), name='history'),
    path('mission/', MissionView.as_view(), name='mission'),
    path('team/', TeamView.as_view(), name='team'),

    # path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    # path('', ArticlesListView.as_view(), name='article_list'),
    # path('create/', ArticleCreateView.as_view(), name='article_create'),
    # path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    # path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),

]
