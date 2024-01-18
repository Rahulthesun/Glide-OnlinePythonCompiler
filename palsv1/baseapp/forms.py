from django import forms


class AnswerCodeForm(forms.Form):
    answer_code = forms.CharField(widget=forms.Textarea(attrs={'class': 'code-editor'}))
    input = forms.CharField(widget=forms.Textarea(attrs={'class': 'input','required':False}))