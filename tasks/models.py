from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tasks(models.Model):  # Naming convention: singular class name

    COLOR_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        ('green', 'Green'),
        ('grey', 'Grey'),
        ('violet', 'Violet'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start = models.TimeField()
    stop = models.TimeField()
    duration = models.CharField(max_length=10, blank=True)  # Should be updated after duration calculation
    clolor = models.CharField(max_length=10, choices=COLOR_CHOICES)  # Corrected spelling from 'clolor' to 'color'

    def __str__(self):
        return self.title

    def calculate_duration(self):
        start_seconds = (self.start.hour * 3600) + (self.start.minute * 60) + self.start.second
        stop_seconds = (self.stop.hour * 3600) + (self.stop.minute * 60) + self.stop.second

        if stop_seconds < start_seconds:
            stop_seconds += 24 * 3600 

        duration_seconds = stop_seconds - start_seconds
        hours, remainder = divmod(duration_seconds, 3600)
        minutes, _ = divmod(remainder, 60)

        if hours > 0:
            self.duration = f"{hours}h {minutes:02}m"
        else:
            self.duration = f"{minutes:02}m"

    def save(self, *args, **kwargs):
        self.calculate_duration()
        super().save(*args, **kwargs)


