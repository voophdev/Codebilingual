from django import forms
from .models import PythonQuestion, CppQuestion

class PythonQuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        quiz = kwargs.pop('quiz', None)
        if quiz is None:
            raise ValueError("Quiz object is required for initializing the form")
        super().__init__(*args, **kwargs)
        
        # print(f"Initializing PythonQuizForm for quiz: {quiz}")  # Debug
        
        for question in quiz.questions.all():
            # print(f"Question: {question}")  # Debug
            choices = [(choice.id, choice.text) for choice in question.choices.all()]
            # print(f"Choices: {choices}")  # Debug
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=choices, widget=forms.RadioSelect, label=question.text
            )

class CppQuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        quiz = kwargs.pop('quiz', None)
        if quiz is None:
            raise ValueError("Quiz object is required for initializing the form")
        super().__init__(*args, **kwargs)
        
        # print(f"Initializing CppQuizForm for quiz: {quiz}")  # Debug
        
        for question in quiz.questions.all():
            # print(f"Question: {question}")  # Debug
            choices = [(choice.id, choice.text) for choice in question.choices.all()]
            # print(f"Choices: {choices}")  # Debug
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                choices=choices, widget=forms.RadioSelect, label=question.text
            )
