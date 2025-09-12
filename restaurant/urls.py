from django.urls import path

# from restaurant import views
from restaurant.apps import RestaurantConfig
from restaurant.views import SectionDetailView

#     MainDescriptionView, MainServicesView, MainContactsView, AboutFeedbackView, AboutHistoryView, AboutMissionView, \
#     AboutTeamView,

# from restaurant.views import DescriptionView, ContactsView, ServicesView, FeedbackView, HistoryView, MissionView, TeamView

# , BlogContactsView, ArticleDetailView, ArticlesListView, ArticleCreateView, \
#     ArticleUpdateView, ArticleDeleteView)

app_name = RestaurantConfig.name

urlpatterns = [
    # path('', HomePageView.as_view(), name='home_page'),

    path('section/<int:pk>/', SectionDetailView.as_view(), name='section_detail'),
    # path('main/description/<int:pk>/', MainDescriptionView.as_view(), name='main_description'),
    # path('main/contacts/<int:pk>/', MainContactsView.as_view(), name='main_contacts'),
    # path('main/services/<int:pk>/', MainServicesView.as_view(), name='main_services'),
    # path('section/feedback/', MainFeedbackView.as_view(), name='main_feedback'),
    # path('about/history/<int:pk>/', AboutHistoryView.as_view(), name='about_history'),
    # path('about/mission/<int:pk>/', AboutMissionView.as_view(), name='about_mission'),
    # path('about/team/<int:pk>/', AboutTeamView.as_view(), name='about_team'),
    # path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    # path('', ArticlesListView.as_view(), name='article_list'),
    # path('create/', ArticleCreateView.as_view(), name='article_create'),
    # path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
    # path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),

]
