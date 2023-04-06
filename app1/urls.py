from django.urls import path 
from .views import StudentDetail, StudentInfo, FeedbackDetail, FeedbackInfo

urlpatterns = [
    path("submit/",StudentDetail.as_view(), name="submit"),
    path("submit/<int:id>/",StudentInfo.as_view()),
    path("submitFeedback/", FeedbackDetail.as_view(), name="submitFeedback"),
    path("submitFeedback/<int:id/",FeedbackInfo.as_view()),
]
