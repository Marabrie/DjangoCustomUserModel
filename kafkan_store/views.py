from django.shortcuts import render, redirect, get_object_or_404
from .models import Kafkan
from .forms import KafkanForm



def kafkan_list(request):
    kafkans = Kafkan.objects.all()
    return render(request, "kafkan_list.html", {'kafkans': kafkans})

def home(request):
    return render(request, "home.html",)

def kafkan_detail(request, pk):
    kafkan = get_object_or_404(Kafkan, pk=pk)
    return render(request, "kafkan_detail.html", {'kafkan': kafkan})

def kafkan_new(request):
    if request.method == "POST":
        form = KafkanForm(request.POST)
        if form.is_valid():
            kafkan = form.save()
            return redirect("kafkan_detail", pk=kafkan.pk)
    else:
        form = KafkanForm
    return render(request, "kafkan_create.html", {'form': form})

def kafkan_edit(request, pk):
    kafkan = get_object_or_404(Kafkan, pk=pk)
    if request.method == "GET":
        form = KafkanForm( instance=kafkan)
    else:
        form = KafkanForm(request.POST, instance=kafkan)
        if form.is_valid():
            form.save()
            return redirect("kafkan_list")

    return render(request, "kafkan_edit.html", {"form": form, "kafkan": kafkan})
   

def kafkan_delete(request, pk):
    kafkan = get_object_or_404(Kafkan, pk=pk)
    if request.method == "POST":
        kafkan.delete()
        return redirect("kafkan_list")
    return render(request, "kafkan_delete.html", {"kafkan": kafkan})


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

 