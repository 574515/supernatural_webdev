from django.contrib import admin
from django.urls import include, path

#from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetView,
    PasswordResetCompleteView,
)
from django.urls.base import reverse_lazy


from account.views import (
    AccountView,
    LoginView,
    LogoutView,
    MustAuthenticateView,
    RegisterView,
)

app_name = 'account'

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('must_authenticate/', MustAuthenticateView, name='must_authenticate'),
    path('register/', RegisterView, name='register'),
    path('profile/<int:user_id>', AccountView, name='profile'),
    # Password Change Forms (import from Django Auth)
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_change/', PasswordChangeView.as_view(template_name='registration/password_change.html', success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    
    path('password_reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),
]