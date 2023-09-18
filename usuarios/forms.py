from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome', 
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={            
                "class" : "form-control",
                "placeholder" : "Usuário"
            }
        )
    )

    senha = forms.CharField(
        label='Senha', 
        required=True,
        max_length=30,
        widget=forms.PasswordInput(
            attrs={     
                "class" : "form-control",          
                "placeholder" : "Digite sua Senha"
            }
        )
    )