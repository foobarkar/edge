from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
from . import views

urlpatterns = [
    path(r'', views.HomePage.as_view(), name='home'),
    path(r'about/', views.AboutPage.as_view(), name='about'),
    path(r'users/', include(profiles.urls, namespace='profiles')),
    path(r'admin/', admin.site.urls),
    path(r'', include(accounts.urls, namespace='accounts')),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Include django debug toolbar if DEBUG is on
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path(r'__debug__/', include(debug_toolbar.urls)),
    ]
