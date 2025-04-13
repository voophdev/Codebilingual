from django.contrib import admin
from .models import PythonQuiz, PythonQuestion, PythonChoice, PythonResult, CppQuiz, CppQuestion, CppChoice, CppResult, CppQuizCompletion, PythonQuizCompletion

admin.site.register(PythonQuiz)
admin.site.register(PythonQuestion)
admin.site.register(PythonChoice)
admin.site.register(PythonResult)
admin.site.register(CppQuiz)
admin.site.register(CppQuestion)
admin.site.register(CppChoice)
admin.site.register(CppResult)
admin.site.register(CppQuizCompletion)
admin.site.register(PythonQuizCompletion)
