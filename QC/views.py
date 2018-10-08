from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Material


# Create your views here.

def index(request):
    material_list = Material.objects.all
    context = {
        'material_list': material_list,
        }
    return render(request, 'QC/index.html', context)


def detail(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    return render(request, 'QC/detail.html', {'material': material})


def process(request, material_id):
    material = get_object_or_404(Material, pk=material_id)
    decision = ""
    try:
        if 'Accept' in request.POST:
            decision = "accepted"
        elif 'Reject' in request.POST:
            decision = "rejected"

    except (KeyError, material.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'QC/detail.html', {
            'Material': material,
            'error_message': "You didn't select a choice.",
        })
    else:
        material.status = decision
        material.save()

        return HttpResponseRedirect(reverse('QC:index'))
