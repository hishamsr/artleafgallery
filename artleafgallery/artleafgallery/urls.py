
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf import settings

from rest_framework import routers
from rest_framework.authtoken import views
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope

from gallery import views as gallery_views
from authentication import views as authentication_views


admin.autodiscover()





router = routers.DefaultRouter()
router.register(r'users', authentication_views.UserViewSet)
router.register(r'groups', authentication_views.GroupViewSet)
router.register(r'api/products', gallery_views.ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^sign_up/$', authentication_views.SignUp.as_view(), name="sign_up"),
]


# ... your normal urlpatterns here
print(settings.DEBUG)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))