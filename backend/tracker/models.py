from django.db import models


class EmailStatus(models.Model):
    email = models.EmailField()
    tracking_hash = models.CharField(max_length=64, unique=True)
    status = models.CharField(
        max_length=20,
        choices=[("sent", "Sent"), ("opened", "Opened"), ("failed", "Failed")],
        default="sent",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email} - {self.status}"
