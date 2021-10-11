from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Kafkan
from .forms import KafkanForm
from django.shortcuts import redirect
#from django.http import HttpResponse


def kafkan_list(request):
    kafkan = Kafkan.objects.order_by('size', 'price', 'color', 'material')
    return render(request, 'kafkan_list.html')

def home(request):
    return render(request, 'home.html',)

def kafkan_detail(request, pk):
    kafkan = get_object_or_404(Kafkan, pk=pk)
    return render(request, 'kafkan_detail.html', {'kafkan': kafkan})

def kafkan_new(request):
    if request.method == 'POST':
        form = KafkanForm(request.POST)
        if form.is_valid():
            kafkan = form.save(commit=False)
            kafkan.author = request.user
            kafkan.save()
            return redirect('kafkan_detail', pk=kafkan.pk)
    else:
        form = KafkanForm
    return render(request, 'kafkan_edit.html', {'form': form})

def kafkan_edit(request, pk):
    kafkan = get_object_or_404(Kafkan, pk=pk)
    if request.method == 'POST':
        form = KafkanForm(request.POST, instance=kafkan)
        if form.is_valid():
            kafkan = form.save(commit=False)
            kafkan.author = request.user
            kafkan.save()
            return redirect('kafkan_edit', pk=kafkan.pk)
    else:
        form = KafkanForm(instance=kafkan)
    return render(request, 'kafkan_edit.html', {'form': form})

def kafkan_delete(request, pk):
    kafkan_to_delete = get_object_or_404(Kafkan, pk=pk)
    kafkan_to_delete.delete()
    return redirect('kafkan_list')


# def create_kafkan(request):
#     if request.method == "GET":
#         form = KafkanForm()
#         return render(request, 'kafkan/create_kafkan.html', {'form':form})
#     elif request.method == "POST":
#         form = KafkanForm(request.POST)
#         if form.is_valid():
#             size = form.data['size']
#             price = form.data['price']
#             color = form.data['color']
#             material = form.date['material']
#             validated_kafkan = Kafkan.objects.get_or_create(kafkan=kafkan)[0]
#             Kafkan = kafkan.objects.create(kafkan=validated_kafkan)
#             Kafkan.save()
#             return redirect('_list', pk=kafkan.pk)

 