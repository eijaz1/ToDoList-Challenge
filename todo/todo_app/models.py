from django.db import models

# Create your models here.

class ToDoItem(models.Model):

    STATUS_CHOICES = [
        ('On Time', 'On Time'),
        ('Complete', 'Complete'),
        ('Expected Late', 'Expected Late'),
        ('Overdue', 'Overdue'),
    ]

    # STATUS_CHOICES = [
    #     ('on_time', 'On Time'),
    #     ('complete', 'Complete'),
    #     ('expected_late', 'Expected Late'),
    #     ('overdue', 'Overdue'),
    # ]

    title                   = models.CharField(max_length=200)
    description             = models.TextField(max_length=1000)
    status                  = models.CharField(max_length=20, choices=STATUS_CHOICES)
    due_date                = models.DateField()

    def __str__(self):
        return self.title


