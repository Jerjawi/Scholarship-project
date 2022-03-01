from django.urls import path
from .views import Marks_list, Marks_Create,Marks_Update, Mark_Detail,Mark_Delete,super_user_marks
urlpatterns = [
    path('<str:username>/' ,Marks_list.as_view(), name = 'specific_marks'),
    path('update_mark/<int:pk>/',Marks_Update.as_view(), name = 'Marks_Update'),
    path('detail/<int:pk>/',Mark_Detail.as_view(), name = 'Mark_Detail'),
    path('delete_mark/<int:pk>/',Mark_Delete.as_view(), name = 'Marks_delete'),
    path('create', Marks_Create.as_view(), name='mark_create'),
    path('superuser_marks',super_user_marks, name = 'superuser_marks')
    

]

