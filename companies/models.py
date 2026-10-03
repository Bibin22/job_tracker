from django.db import models

# Create your models here.

from django.conf import settings


class Company(models.Model):
    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="companies",
    )

    name = models.CharField(max_length=500)
    description = models.TextField(blank=True)
    website = models.URLField(max_length=500, blank=True)
    location = models.CharField(max_length=500, blank=True)
    logo = models.URLField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "companies"
        constraints = [
            models.UniqueConstraint(
                fields=["recruiter", "name"],
                name="unique_company_name_per_recruiter",
            )
        ]
