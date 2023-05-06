from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound , Http404
# Create your views here.
from django.view.generic import TemplateView , CreateView, ListView ,DetailView


class HomePage(TemplateView):
    template_name = "student.html"
    


# def student(request, number1, number2 ):
#     try:
#         res=number1+number2
#         return HttpResponse(res)
#     except:
#         res="con't sum number with string "
#         # return HttpResponseNotFound(res)
#         raise Http404("404 ERROR ")
    
def student(request):
    return render(request , 'student.html')


#########################   

def Add(request):
    return render(request , 'add.html')


#########################


def Edit(request):
    return render(request , 'edit.html')