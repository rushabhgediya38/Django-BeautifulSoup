from django.db import models


class sData(models.Model):
    eventAttendanceMode = models.CharField(max_length=256, blank=True, null=True)
    name = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    startDate = models.DateTimeField(blank=True, null=True)
    endDate = models.DateTimeField(blank=True, null=True)
    performer_name = models.CharField(max_length=256, blank=True, null=True)
    category = models.CharField(max_length=256, default="Noting", blank=True, null=True)

    def __str__(self):
        return str(self.name)


class InterestingUrl(models.Model):
    Interesting_url1 = models.URLField(blank=True, null=True)

    def __str__(self):
        return str(self.Interesting_url1)


class Non_interesting_url(models.Model):
    Non_interesting_url1 = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.Non_interesting_url1)
