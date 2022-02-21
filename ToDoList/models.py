from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.

STATUS_CHOICES = (
    ('OPEN', 'OPEN'),
    ('WORKING', 'WORKING'),
    ('DONE', 'DONE'),
    ('OVERDUE', 'OVERDUE')
)


class Tags(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)


class ListModel(models.Model):
    id = models.AutoField(primary_key=True)
    Timestamp = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        help_text='Created at'
    )
    Title = models.CharField(max_length=100, blank=False)
    Description = models.CharField(max_length=1000, blank=False)
    Tag = models.ManyToManyField(Tags, blank=True)
    Status = models.CharField(
        max_length=7,
        choices=STATUS_CHOICES,
        default='OPEN',
        blank=False
    )

    def __str__(self):
        return self.Title

    def tags(self):
        return ", ".join([p.title for p in self.Tag.all()])

    def validate_date(DueDate):
        if DueDate < timezone.now().date():
            raise ValidationError("Due-Date cannot be before event created")
   
    DueDate = models.DateField(null=True, blank=True, default=None, validators=[validate_date])

    class Meta:
        ordering = ('id',)
