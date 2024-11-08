import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Dataset
from projects.models import Project  # Add this import
import os

@login_required
def dataset_list(request):
    datasets = Dataset.objects.filter(project__user=request.user)
    return render(request, 'etl/dataset_list.html', {'datasets': datasets})

@login_required
def dataset_upload(request):
    if request.method == 'POST':
        file = request.FILES['dataset_file']
        
        # Verify file is CSV
        if not file.name.endswith('.csv'):
            messages.error(request, 'Please upload a CSV file')
            return redirect('dataset_upload')
            
        try:
            # Read CSV and validate
            df = pd.read_csv(file)
            
            # Create dataset record
            dataset = Dataset.objects.create(
                project_id=request.POST['project_id'],
                name=request.POST['name'],
                file=file
            )
            
            # Save DataFrame info in session or cache for later use
            request.session[f'dataset_{dataset.id}_columns'] = df.columns.tolist()
            request.session[f'dataset_{dataset.id}_shape'] = df.shape
            
            messages.success(request, 'Dataset uploaded successfully')
            return redirect('dataset_list')
            
        except Exception as e:
            messages.error(request, f'Error processing file: {str(e)}')
            return redirect('dataset_upload')
    
    # GET request - show upload form
    projects = Project.objects.filter(user=request.user)
    return render(request, 'etl/dataset_upload.html', {'projects': projects})
