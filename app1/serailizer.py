from rest_framework import serializers
from .models import Student, Feedback

class StudentSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        
class FeedbackSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = "__all__"