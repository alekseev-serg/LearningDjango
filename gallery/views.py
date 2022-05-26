from django.shortcuts import render, redirect
from .models import Pictures
from .forms import LoadForm


# Create your views here.
def gallery_index(request):
    if request.method == 'POST':
        form = LoadForm(request.POST, request.FILES)
        if form.is_valid():
            pic_upl = Pictures()
            pic_upl.images = request.FILES['images']
            pic_upl.title = pic_upl.images.name
            pic_upl.save()
            return redirect('gallery')
    else:
        form = LoadForm()
    pictures = Pictures.objects.all()
    return render(request, 'gallery/gallery_index.html', {'form': form,
                                                  'pictures': pictures})
