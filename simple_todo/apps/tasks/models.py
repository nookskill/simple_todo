from django.db import models


class Task(models.Model):
    PENDING = 'pending'
    DONE = 'done'

    TASK_STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (DONE, 'Done')
    )

    subject = models.CharField(max_length=255, verbose_name='Subject')
    content = models.TextField(blank=True, null=True, verbose_name='Content')
    status = models.CharField(default=PENDING, choices=TASK_STATUS_CHOICES, verbose_name='Status')

    class Meta:
        verbose_name = 'Task'

    def __str__(self):
        return f'subject: {self.subject}'
