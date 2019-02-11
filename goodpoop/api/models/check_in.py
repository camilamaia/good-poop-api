from django.db import models
from goodpoop.api.models import Account, Restroom


class CheckIn(models.Model):
    restroom = models.ForeignKey(
        Restroom, on_delete=models.CASCADE, related_name="check_ins"
    )
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="check_ins"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
