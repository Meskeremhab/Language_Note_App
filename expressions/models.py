from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

REGISTERS = [
    ('neutral', 'Neutral'),
    ('informal', 'Informal'),
    ('slang', 'Slang'),
    ('formal', 'Formal'),
]

class Expression(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expressions')
    text = models.CharField(max_length=200)
    meaning = models.TextField()
    region = models.CharField(max_length=120, blank=True)   # e.g. "Madrid", "US", "Ethiopia"
    register = models.CharField(max_length=20, choices=REGISTERS, default='neutral')
    usage_notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['text']
        unique_together = ('owner', 'text')

    def __str__(self):
        return self.text
