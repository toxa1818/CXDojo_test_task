from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from datetime import datetime
from .forms import UploadFilesForm
from .models import File
from .validation import get_info_from_files, update_db


@login_required
def index(request):
    user = get_user_model()
    data = get_info_from_files()
    for user_data in data:
        if not user.objects.filter(username=user_data['username']):
            user.objects.create(
                username=user_data['username'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                date_joined=datetime.fromtimestamp(int(user_data['date_joined'])),
            )
        valid_user = user.objects.get(username=user_data["username"])
        valid_user.set_password(user_data["password"])
        valid_user.save()

    context = {'users': user.objects.all()}
    return render(request, 'index.html', context)


def upload_files(request):
    if request.POST:
        form = UploadFilesForm(request.POST, request.FILES)
        csv_file = request.FILES['upload_csv_file']
        xml_file = request.FILES['upload_xml_file']
        if form.is_valid():
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'Not csv type')
                return HttpResponseRedirect(reverse_lazy('includes:upload'))
            if not xml_file.name.endswith('.xml'):
                messages.error(request, 'Not xml type')
                return HttpResponseRedirect(reverse_lazy('includes:upload'))
            new_files = File(csv_file=csv_file, xml_file=xml_file)
            update_db()
            new_files.save()
            return HttpResponseRedirect(reverse_lazy('includes:index'))
    else:
        form = UploadFilesForm()

    return render(request, 'upload_files.html', context={'form': form})



