from django import forms
from .models import Users, Response, Questions


"""class for create form with models class """


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'