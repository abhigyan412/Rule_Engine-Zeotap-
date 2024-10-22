from django.db import models

class Rule(models.Model):
    rule_string = models.TextField()  # Stores the rule as a string
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for the last update
    description = models.CharField(max_length=255, blank=True)  # Optional field for rule description
    is_active = models.BooleanField(default=True)  # Field to mark if the rule is active

    def __str__(self):
        return self.rule_string

    class Meta:
        verbose_name = 'Rule'
        verbose_name_plural = 'Rules'
        ordering = ['created_at']  # Order rules by creation date
