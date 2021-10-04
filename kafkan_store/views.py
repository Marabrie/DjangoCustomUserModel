from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Kafkan
from .forms import KafkanForm
from django.shortcuts import redirect
#from django.http import HttpResponse


def kafkan_list(request):
    kafkan = Kafkan.objects.order_by('size', 'price', 'color', 'material')
    return render(request, 'kafkan/kafkan_list.html', {'kafkan': kafkan})

def kafkan_detail(request, pk):
    kafkan = get_object_or_404(Kafkan, pk=pk)
    return render(request, 'kafkan/kafkan_detail.html', {'kafkan': kafkan})

def kafkan_new(request):
    if request.method == 'POST':
        form = KafkanForm(request.POST)
        # kafkan_form = KafkanForm(request.POST)
        if form.is_valid():
            kafkan = form.save(commit=False)
            kafkan.author = request.user
            kafkan.save()
            return redirect('kafkan_detail', pk=kafkan.pk)
    else:
        form = KafkanForm
    return render(request, 'kafkan/kafkan_edit.html', {'form': form})