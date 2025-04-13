from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class LessonCPP(models.Model):
    lesson = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    banner = models.ImageField(default='cpp.png', blank=True)
    is_finished = models.BooleanField(default=False)
    slug = models.SlugField(default='')  
    id = models.AutoField(primary_key=True)
    previous_lesson = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

class LessonPY(models.Model):
    lesson = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    banner = models.ImageField(default='py.png', blank=True)
    is_finished = models.BooleanField(default=False)
    slug = models.SlugField(default='')  
    id = models.AutoField(primary_key=True)
    previous_lesson = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

class LessonCompletion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    lesson_cpp = models.ForeignKey(LessonCPP, null=True, blank=True, on_delete=models.CASCADE)
    lesson_py = models.ForeignKey(LessonPY, null=True, blank=True, on_delete=models.CASCADE)
    completed = models.BooleanField(default=True)
    completion_date = models.DateTimeField(auto_now_add=True)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_lesson_completion(sender, instance, created, **kwargs):
    if created and instance.role == 'student':
        LessonCompletion.objects.create(user=instance)
