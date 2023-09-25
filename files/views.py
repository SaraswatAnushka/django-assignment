from django.http import HttpResponse
from django.shortcuts import render
from .forms import MyfileUploadForm
from .models import file_Upload


def index(request):

    if request.method=='POST':
        c_form = MyfileUploadForm(request.POST, request.FILES)

        if c_form.is_valid():
            name = c_form.cleaned_data['file_name']
            files = c_form.cleaned_data['files_data']
            file_Upload(file_name= name,my_files = files).save()

            return HttpResponse('File uploaded successfully')
        else:
            return HttpResponse('Error in uploading files')
    else:
        context={
        'form' :MyfileUploadForm(),
    }

    
    return render(request,'files/index.html',context)

def show_files(request):
    all_data = file_Upload.objects.all
    context={
        'data':all_data
            }
    return render(request,'files/view.html',context)




# Create your views here.
