from django.db import models


class TeamMember(models.Model):
    POSITION_CHOICE = [
        ('duelist', 'Duelist'),
        ('controller', 'Controller'),
        ('sentinel', 'Sentinel'),
        ('initiator', 'Initiator'),
    ]

    riot_ID = models.CharField(max_length=30)
    experience = models.PositiveIntegerField(default=0)
    position = models.CharField(max_length=30, choices=POSITION_CHOICE)
    statistics = models.URLField()
    discord = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.riot_ID

