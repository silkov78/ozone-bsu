from django.urls import path
from django.views.generic import RedirectView

from .views import worker_page

# html-страницы (внутри i18n_patterns)
urlpatterns = [
    path('staff/<int:pk>/', worker_page, name='workers-detail-url'),
    path('staff/', RedirectView.as_view(url='/about/#team', permanent=True), name='workers-list-url'),
]
