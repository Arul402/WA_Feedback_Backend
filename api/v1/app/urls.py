from django.urls import path
from .views import example_view,create_feedback,get_feedbacks,get_feedback,update_feedback,delete_feedback

urlpatterns = [
    path('example/', example_view),  
    # path('feedback/', FeedbackCreateView.as_view(), name='feedback-create'),
    path('feedback/', create_feedback, name='create-feedback'),  
    path('feedbacks/', get_feedbacks, name='get-feedbacks'),  
    path('feedback/<int:pk>/', get_feedback, name='get-feedback'),  
    path('feedback/update/<int:pk>/', update_feedback, name='update-feedback'),  
    path('feedback/delete/<int:pk>/', delete_feedback, name='delete-feedback'),  
]
