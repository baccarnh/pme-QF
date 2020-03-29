from django import forms
from .models import Users, Response, Questions


"""class for create form with models class """


class ResponseForm(forms.ModelForm):
    # i use classe for extend the model for create a form based in this
    class Meta:
        model = Response
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    # i use classe for extend the model for create a form based in this
    class Meta:
        model = Questions
        fields = '__all__'