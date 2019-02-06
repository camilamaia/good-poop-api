from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Account(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Restroom(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_by = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="created_restrooms",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CheckIn(models.Model):
    restroom = models.ForeignKey(
        Restroom, on_delete=models.CASCADE, related_name="check_ins"
    )
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="check_ins"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    FEMALE = "female"
    MALE = "male"
    UNISEX = "unisex"
    ACCESSIBLE = "accessible"
    FEMALE_ACCESSIBLE = "accessible"
    MALE_ACCESSIBLE = "accessible"
    CATEGORY_CHOICES = (
        (FEMALE, "Female"),
        (MALE, "Male"),
        (UNISEX, "Unissex"),
        (ACCESSIBLE, "Unissex Accessible"),
        (MALE_ACCESSIBLE, "Male Accessible"),
        (FEMALE_ACCESSIBLE, "Female Accessible"),
    )

    restroom = models.ForeignKey(
        Restroom, on_delete=models.CASCADE, related_name="reviews"
    )
    account = models.ForeignKey(
        Account,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="reviews",
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_free = models.BooleanField(default=True)

    comment = models.TextField(null=True, blank=True)
    cleanness_rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True
    )
    soundproofing_rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True
    )
    soap_quality_rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True
    )
    drying_hands_quality_rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True
    )
    flush_power_rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True
    )
    touchless_rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True
    )
    ecological_rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True
    )
    accessible_rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, blank=True
    )

    has_toilet_brush = models.NullBooleanField()
    has_touchless_sink = models.NullBooleanField()
    has_touchless_flush = models.NullBooleanField()
    has_touchless_doors = models.NullBooleanField()
    is_public = models.NullBooleanField()
    has_soap = models.NullBooleanField()
    has_towel_paper = models.NullBooleanField()
    has_hand_dryer = models.NullBooleanField()
    has_roller_towels = models.NullBooleanField()
    price = models.FloatField(
        validators=[MinValueValidator(0.0)], null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
