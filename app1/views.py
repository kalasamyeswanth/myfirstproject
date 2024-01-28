from django.shortcuts import render

# Create your views here.
def fun_name(request):
    dd={'a':'yeswanth','b':'madhu priya'}
    return render(request,'code.html',context=dd)