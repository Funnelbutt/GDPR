from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from .forms import UploadImageForm
from django.core.files.storage import FileSystemStorage

def data_view(request):
    return render(request, 'redaction_webapp/templates/redaction_webapp/data_view.html', {})

def uimage(request):
    form = UploadImageForm(request.POST, request.FILES or None)
    if request.method == 'POST':

        if form.is_valid():
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'redaction_webapp/uimage.html', {'form': form, 'uploaded_file_url': uploaded_file_url})
    else:
        form = UploadImageForm()
        return render(request, 'redaction_webapp/uimage.html', {'form': form})
