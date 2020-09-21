from django.conf.urls import url
from .views import signup
from django.contrib.auth import views as auth_views


urlpatterns = [url(r'^signup/', signup,  name = 'sign-up'),
                url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
                url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
                url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name='password_reset'),
                url(r'^password_reset/done/$', auth_views.PasswordResetDoneView, name='password_reset_done'),
                url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                auth_views.PasswordResetConfirmView, name='password_reset_confirm'),
                url(r'^reset/done/$', auth_views.PasswordChangeDoneView, name='password_reset_complete'),
               ]

