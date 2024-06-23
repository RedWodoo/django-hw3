from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'bboard/index.html')

def index2(request):
    return render(request,'bboard/login.html')



def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    return render(request, 'bboard/login.html')
