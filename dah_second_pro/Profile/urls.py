from .views import Protofile,Profile_Create,Profile_Update,all_profiles
from django.urls import path

urlpatterns = [
    path('<int:pk>/detail/',Protofile.as_view(), name=  'detail_profile'),
    path('create_profile',Profile_Create.as_view(), name = 'create_profile'),
    path('<int:pk>/update/',Profile_Update.as_view(), name=  'profile_update'),
    path('all_profile', all_profiles, name = 'all_profiles')
    
]