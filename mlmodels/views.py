from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import MLModel
from etl.models import Dataset
import json
import joblib
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.svm import SVC
from sklearn.cluster import KMeans
import pandas as pd

@login_required
def model_list(request):
    models = MLModel.objects.filter(dataset__project__user=request.user)#, dataset__project=request.project)
    # models = MLModel.objects.filter(dataset__project=project)
    return render(request, 'mlmodels/model_list.html', {'models': models})

@login_required
def model_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        dataset_id = request.POST['dataset_id']
        model_type = request.POST['model_type']
        algorithm = request.POST['algorithm']
        
        # Parse hyperparameters from form
        hyperparameters = {}
        for key, value in request.POST.items():
            if key.startswith('hyperparameters.'):
                param_name = key.split('.')[1]
                hyperparameters[param_name] = value

        # Create ML model instance
        model = MLModel.objects.create(
            name=name,
            dataset_id=dataset_id,
            model_type=model_type,
            algorithm=algorithm,
            hyperparameters=hyperparameters
        )

        # Train the model
        train_model(model)
        
        return redirect('model_list')
    
    # GET request - show form
    datasets = Dataset.objects.filter(project__user=request.user)
    return render(request, 'mlmodels/model_create.html', {'datasets': datasets})

def train_model(model):
    # Load dataset
    dataset = pd.read_csv(model.dataset.file.path)
    
    # Assume last column is target (you might want to make this configurable)
    X = dataset.iloc[:, :-1]
    y = dataset.iloc[:, -1]
    
    # Initialize the appropriate algorithm
    if model.algorithm == 'linear_regression':
        ml_model = LinearRegression(**model.hyperparameters)
    elif model.algorithm == 'logistic_regression':
        ml_model = LogisticRegression(**model.hyperparameters)
    elif model.algorithm == 'random_forest':
        if model.model_type == 'regression':
            ml_model = RandomForestRegressor(**model.hyperparameters)
        else:
            ml_model = RandomForestClassifier(**model.hyperparameters)
    elif model.algorithm == 'svm':
        ml_model = SVC(**model.hyperparameters)
    elif model.algorithm == 'kmeans':
        ml_model = KMeans(**model.hyperparameters)
    
    # Train the model
    ml_model.fit(X, y)
    
    # Save the trained model
    model_path = f'ml_models/{model.id}_model.joblib'
    joblib.dump(ml_model, model_path)
    
    # Update model instance
    model.trained = True
    model.model_file = model_path
    
    # Calculate and save metrics
    metrics = calculate_metrics(ml_model, X, y, model.model_type)
    model.metrics = metrics
    model.save()

def calculate_metrics(ml_model, X, y, model_type):
    metrics = {}
    if model_type == 'regression':
        metrics['r2_score'] = ml_model.score(X, y)
    elif model_type == 'classification':
        metrics['accuracy'] = ml_model.score(X, y)
    elif model_type == 'clustering':
        metrics['inertia'] = ml_model.inertia_
    return metrics

@login_required 
def model_delete(request, model_id):
    model = MLModel.objects.get(id=model_id, dataset__project__user=request.user)
    
    # Delete the saved model file if it exists
    if model.model_file:
        import os
        if os.path.exists(model.model_file):
            os.remove(model.model_file)
    
    # Delete the model from database
    model.delete()
    
    return redirect('model_list')