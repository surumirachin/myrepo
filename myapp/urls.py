from django.urls import path,include
from . import views

# urlpatterns = [
#     path('',views.index,name = 'index')
# ]
urlpatterns = [
    path('myapp/',views.Question_list,name ='question_list'),
    path('myapp/question/<int:pk>/',views.Choice_list , name= 'choice_list')
]  

