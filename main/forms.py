from django import forms


class Userform(forms.Form):
    name = forms.CharField(label="Имя", min_length=2)
    age = forms.IntegerField(label="Возраст")
    email = forms.EmailField(label="Электронная почта")
