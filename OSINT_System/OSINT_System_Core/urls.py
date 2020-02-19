from django.urls import path
from OSINT_System_Core import views
#from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'OSINT_System_Core'

urlpatterns = [
    path('',views.Main.as_view(),name = 'main_page'),
    #path('target_author_main/',views.Target_Author_Main.as_view(),name = 'target_author_main'),
    path('target_headlines_main/',views.Target_Headlines_Main.as_view(),name = 'target_headlines_main'),
    path('supported_site_list/',views.Supported_Social_Site_List.as_view(),name = 'supported_site_list'),
    path('add_news_target/',views.News_Target.as_view(),name='add_news_target'),
    path('add_instagram_target/', views.Add_Instagram_Target.as_view(), name='add_instagram_target'),
    path('add_twitter_target/', views.Add_Twitter_Target.as_view(), name='add_twitter_target'),
    path('add_facebook_target/', views.Add_Facebook_Target.as_view(), name='add_facebook_target'),
    path('add_linkedin_target/', views.Add_Linkedin_Target.as_view(), name='add_linkedin_target'),

    path('article_stat_overview',views.Article_Stat_Overview.as_view(),name='article_stat_overview'),
    path('article_stat_slo',views.Article_Stat_Slo.as_view(),name='article_stat_slo'),
    path('my_article_stat',views.My_Article_Stat.as_view(),name='my_article_stat'),
    path('ticket_stat',views.Ticket_State.as_view(),name='ticket_stat'),
    path('fetch_stat',views.Fetch_State.as_view(),name='fetch_stat'),
    path('extracted_article',views.Extracted_Article.as_view(),name='extracted_article'),
    path('extracted_selected_all_site',views.Extracted_All_Sites.as_view(),name='extracted_selected_all_site'),
    path('extracted_selected_all_social_sites',views.Extracted_All_Social_Sites.as_view(),name='extracted_selected_all_social_sites'),
    path('processed_article',views.Processed_Article.as_view(),name='processed_article'),
    path('article_trend',views.Article_Trend.as_view(),name='article_trend'),
    path('send_to_pco',views.Sent_To_Pco,name='send_to_pco'),
    path('smart_search/<str:author_account>/<str:search_site>/',views.Smart_Search.as_view(),name='smart_search'),
    path('get_facebook_targets',views.Get_Facebook_Targets.as_view(),name='get_facebook_target'),
    path('get_twitter_targets',views.Get_Twitter_Targets.as_view(),name='get_twitter_target'),
    path('get_instagram_targets',views.Get_Instagram_Targets.as_view(),name='get_instagram_target'),
    path('get_linkedin_targets',views.Get_Linkedin_Person_Targets.as_view(),name='get_linkedin_target'),

    path('target_author_instagram/',views.Target_Author_Instagram.as_view(),name = 'target_author_instagram'),
    path('target_author_facebook/',views.Target_Author_Facebook.as_view(),name = 'target_author_facebook'),
    path('target_author_twitter/',views.Target_Author_Twitter.as_view(),name = 'target_author_twitter'),
    path('target_author_linkedin/',views.Target_Author_Linkedin.as_view(),name = 'target_author_linkedin'),
    path('dispatcher/<str:GTR>/<str:author_account>',views.Dispatcher.as_view(),name = 'dispatcher'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
]

#urlpatterns = format_suffix_patterns(urlpatterns)