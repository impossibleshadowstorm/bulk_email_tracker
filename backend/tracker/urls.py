from django.urls import path
from .views import SendBulkEmailView, TrackEmailOpenView

urlpatterns = [
    path("send_bulk_email/", SendBulkEmailView.as_view(), name="send_bulk_email"),
    path("track/", TrackEmailOpenView.as_view(), name="track_email_open"),
]
