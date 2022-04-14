from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", min_length=2, max_length=3, initial="Введите ФИО", help_text="Введите ФИО", )
    age = forms.IntegerField(label="Возраст", initial=18, min_value=3, max_value=120, help_text="Введите возраст" )
    email = forms.EmailField(label="Электронный адрес")
    reklama = forms.BooleanField(label="Согласны получать рекламу", required=False)