from django.urls import path
from django.urls.base import reverse_lazy
from django.contrib.auth.views import (
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetView,
)
from account.views import (
    account_view,
    login_view,
    logout_view,
    must_authenticate_view,
    register_view,
)


app_name = 'account'

urlpatterns = [
    # My urls
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('must_authenticate/', must_authenticate_view, name='must_authenticate'),
    path('profile/<int:user_id>', account_view, name='profile'),
    path('register/', register_view, name='register'),
    # Password Change Forms (import from Django Auth)
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('password_change/', PasswordChangeView.as_view(template_name='registration/password_change.html', success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    path('password_reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),    
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(success_url= reverse_lazy('account:password_reset_complete')), name='password_reset_confirm'),    
    path('password_reset/', PasswordResetView.as_view(success_url = reverse_lazy('account:password_reset_done')), name='password_reset'),    
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]
