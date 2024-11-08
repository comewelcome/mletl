from django.db import models
from etl.models import Dataset

class MLModel(models.Model):
    MODEL_TYPES = [
        ('regression', 'Regression'),
        ('classification', 'Classification'),
        ('clustering', 'Clustering'),
    ]

    ALGORITHM_CHOICES = [
        ('linear_regression', 'Linear Regression'),
        ('logistic_regression', 'Logistic Regression'),
        ('random_forest', 'Random Forest'),
        ('svm', 'Support Vector Machine'),
        ('kmeans', 'K-Means Clustering'),
    ]

    name = models.CharField(max_length=200)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    model_type = models.CharField(max_length=20, choices=MODEL_TYPES)
    algorithm = models.CharField(max_length=20, choices=ALGORITHM_CHOICES)
    hyperparameters = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    trained = models.BooleanField(default=False)
    model_file = models.FileField(upload_to='ml_models/', null=True, blank=True)
    metrics = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.name} - {self.algorithm}"

    class Meta:
        ordering = ['-created_at']
