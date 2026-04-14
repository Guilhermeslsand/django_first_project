# Django Allauth Integration Guide 🚀

Este guia fornece um passo a passo completo para integrar o **django-allauth** em seu projeto Django, cobrindo autenticação local, configurações de segurança e customização.

---

## 1. Instalação

Com seu ambiente virtual ativo, instale o pacote via pip:

```bash
pip install django-allauth
```

## 2. Configurações no settings.py

O allauth depende de vários módulos nativos do Django. Siga a ordem abaixo:

### A. Backends de Autenticação

Permite que o Django reconheça o método de login do Allauth além do admin padrão.

```python
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
```

### B. Aplicativos Instalados

Adicione o núcleo do Allauth e o módulo de sites.

```python
INSTALLED_APPS = [
    # ... apps padrão do django
    'django.contrib.sites',

    # Allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    
    # Provedores Sociais (opcional - descomente para usar)
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.github',
]

SITE_ID = 1
```

### C. Fluxo de Redirecionamento

Defina para onde o usuário será enviado após as ações:

```python
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

## 3. Configuração de URLs

No seu arquivo urls.py principal:

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # Cria as rotas /accounts/login, signup, etc.
]
```

## 4. Configurações Avançadas (Comportamento)

Personalize como o login deve funcionar no seu settings.py:

```python
# Autenticação por e-mail em vez de nome de usuário
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

# Verificação de e-mail (Opções: 'mandatory', 'optional' ou 'none')
ACCOUNT_EMAIL_VERIFICATION = 'optional'

# Backend de e-mail para desenvolvimento (exibe o e-mail no terminal)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

## 5. Banco de Dados

```bash
python manage.py migrate
```

## 6. Customização de Templates 🎨

O Allauth vem com templates básicos. Para usar o seu próprio design (Bootstrap, Tailwind, etc):

1. Crie uma pasta chamada templates na raiz do projeto (se ainda não existir).

2. Dentro dela, crie a estrutura account/.

3. Crie arquivos com os nomes exatos do Allauth para sobrescrevê-los:

    - login.html

    - signup.html

    - password_reset.html

```Plaintext
meu_projeto/
├── templates/
│   └── account/
│       ├── login.html
│       └── signup.html
```

## 7. Verificando as Rotas
Após rodar o servidor (python manage.py runserver), você pode testar as principais rotas:

- Login: http://127.0.0.1:8000/accounts/login/

- Cadastro: http://127.0.0.1:8000/accounts/signup/

- Logout: http://127.0.0.1:8000/accounts/logout/

- Alterar Senha: http://127.0.0.1:8000/accounts/password/change/

## Checklist de Produção 🛡️

- [ ] Alterar ACCOUNT_EMAIL_VERIFICATION para 'mandatory'.

- [ ] Configurar um servidor SMTP real (SendGrid, Mailgun ou Gmail) para envio de e-mails.

- [ ] Configurar o SITE_ID no Admin do Django com o domínio correto do seu site.