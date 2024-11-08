from django.shortcuts import render, redirect
from .models import MLModel
from django.contrib.auth.decorators import login_required

@login_required
def model_list(request):
    models = MLModel.objects.filter(dataset__project__user=request.user)
    return render(request, 'mlmodels/model_list.html', {'models': models})

@login_required
def model_create(request):
    if request.method == 'POST':
        # Handle model creation
        dataset_id = request.POST['dataset_id']
        name = request.POST['name']
        model_type = request.POST['model_type']
        algorithm = request.POST['algorithm']
        
        MLModel.objects.create(
            dataset_id=dataset_id,
            name=name,
            model_type=model_type,
            algorithm=algorithm
        )
        return redirect('model_list')
    return render(request, 'mlmodels/model_create.html')
