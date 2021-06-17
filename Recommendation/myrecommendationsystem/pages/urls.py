from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, re_path

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$',views.register,name="register"),
    url(r'^contact/$',views.contact,name="contact"),
    url(r'^login/$',views.loginuser,name="login"),
    url(r'^logout/$',views.logoutuser,name="logout"),
    url(r'movie/(?P<moviess_id>[\w.@+-/:]+)/$', views.rating, name='rating'), # regex is used here to identify the url id
    url(r'^recommend/$',views.recommended,name='recommend'),

    # re_path(r'^logout/$', auth_views.LogoutView.as_view(),
    #     {'next_page': settings.LOGIN_REDIRECT_URL}, name='logout'),

    re_path(r'^reset_password/$', auth_views.PasswordResetView.as_view(template_name='forgot_password.html'),
        name='password_reset'),
    re_path(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),
        name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_change.html'),
        name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),
        name='password_reset_complete'),
    
]
