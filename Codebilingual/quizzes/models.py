from django.db import models
from authuser.models import UserProfile  # Adjust the import path as necessary

class PythonQuiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    questions = models.ManyToManyField('PythonQuestion', related_name='quizzes')

    def __str__(self):
        return self.title

class PythonQuestion(models.Model):
    text = models.TextField(max_length=255)

    def __str__(self):
        return self.text

class PythonChoice(models.Model):
    question = models.ForeignKey(PythonQuestion, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class PythonResult(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    quiz = models.ForeignKey(PythonQuiz, on_delete=models.CASCADE)
    score = models.FloatField(null=True)
    attempts = models.PositiveIntegerField(default=0)  # New field to track attempts

    def __str__(self):
        return f"{self.user.email} - {self.quiz.title} - {self.score}"

class PythonQuizCompletion(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    quiz = models.ForeignKey(PythonQuiz, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'quiz')

    def __str__(self):
        return f"{self.user.email} - {self.quiz.title} - Completed: {self.completed}"

class CppQuiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    questions = models.ManyToManyField('CppQuestion', related_name='quizzes')

    def __str__(self):
        return self.title

class CppQuestion(models.Model):
    text = models.TextField(max_length=255)

    def __str__(self):
        return self.text

class CppChoice(models.Model):
    question = models.ForeignKey(CppQuestion, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class CppResult(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    quiz = models.ForeignKey(CppQuiz, on_delete=models.CASCADE)
    score = models.FloatField(null=True)
    attempts = models.PositiveIntegerField(default=0)  # New field to track attempts

    def __str__(self):
        return f"{self.user.email} - {self.quiz.title} - {self.score}"

class CppQuizCompletion(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    quiz = models.ForeignKey(CppQuiz, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completion_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'quiz')

    def __str__(self):
        return f"{self.user.email} - {self.quiz.title} - Completed: {self.completed}"
