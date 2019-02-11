import factory
from goodpoop.api import models


class AccountFactory(factory.Factory):
    class Meta:
        model = models.Account


class RestroomFactory(factory.Factory):
    class Meta:
        model = models.Restroom


class CheckInFactory(factory.Factory):
    class Meta:
        model = models.CheckIn


class ReviewFactory(factory.Factory):
    class Meta:
        model = models.Review
