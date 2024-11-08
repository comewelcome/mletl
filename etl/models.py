from django.db import models
from projects.models import Project

class Dataset(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='datasets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-uploaded_at']

class DataTransformation(models.Model):
    TRANSFORMATION_TYPES = [
        ('missing', 'Handle Missing Values'),
        ('normalize', 'Normalize Data'),
        ('encode', 'Encode Categorical'),
        ('scale', 'Scale Features'),
    ]
    
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    transformation_type = models.CharField(max_length=20, choices=TRANSFORMATION_TYPES)
    parameters = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_at']
