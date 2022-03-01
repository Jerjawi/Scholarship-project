from django.urls import path
from .views import Finance_list, Finance_Create,Finance_Detail,Finance_Update,Finance_Delete ,superuser_view
urlpatterns = [
    path('files/<str:username>/',Finance_list.as_view(), name=  'files_of'),
    path('create_file/',Finance_Create.as_view(), name= 'create_file'),
    path('<int:pk>/detail/',Finance_Detail.as_view(), name=  'detail_files'),
    path('update/<int:pk>/',Finance_Update.as_view(), name=  'Finance_Update'),
    path('delete/<int:pk>/',Finance_Delete.as_view(), name=  'Finance_Delete'),
    path('superuser_files',superuser_view,name = 'superuser_view')

]