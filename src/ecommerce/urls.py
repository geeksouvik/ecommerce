
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path
from django.urls import include, re_path

from .views import home_page,about_page,contact_page, login_page, register_page


urlpatterns = [
    path('home/', home_page),
    path('about/', about_page),
    path('contact/', contact_page),
    path('login/', login_page),
    path('register/', register_page),
    path('products/', include("products.urls")),
    #path('products-fbv/', product_list_view),
    #re_path('products-detail/(?P<pk>\d+)/', ProductDetailView.as_view()),
    #re_path('products-detail-fbv/(?P<pk>\d+)/', product_detail_view),
    #re_path('products-detail/(?P<slug>[\w-]+)/', ProductDetailSlugView.as_view()),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)