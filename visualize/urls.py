from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

#register the app namespace
app_name = 'visualize'

urlpatterns = [
    path('', views.chart, name='chart' ),
    path('chart1/', views.chart1, name='chart1' ),
    path('chart2/', views.chart2, name='chart2' ),
    path('chart3/', views.chart3, name='chart3' ),
    path('chart4/', views.chart4, name='chart4' ),
    path('chart5/', views.chart5, name='chart5' ),
    path('upload/',views.upload_json, name='upload_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
