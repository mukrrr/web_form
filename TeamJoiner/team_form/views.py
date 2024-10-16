from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TeamMemberForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def form(request):
    submitted = False
    if request.method == 'POST':
        form = TeamMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/form?submitted=true')
        else:
            print(form.errors)
    else:
        form = TeamMemberForm
        if 'submitted' in request.GET:
            submitted = True

    form = TeamMemberForm
    return render(request,'form.html', {'form': form, 'submitted': submitted})
