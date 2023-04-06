from django.db import models

# Create your models here.

class Student(models.Model):
    studentid = models.IntegerField()
    studentAssignment = models.CharField(max_length=100)
    studentFilePath = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.studentid}--{self.studentAssignment}"

class Feedback(models.Model):
    feedbackAssignment = models.CharField(max_length=200)
    submissionId = models.IntegerField()
    studentId = models.IntegerField()
    assignmentName = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.feedbackAssignment} - Submission ID: {self.submissionId} - Student ID: {self.studentId} - Assignment: {self.assignmentName}"
