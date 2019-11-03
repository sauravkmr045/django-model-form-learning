from django.shortcuts import render
from app2.forms import signupform
# Create your views here.
def index(request):
    return render(request, 'app2/index.html')

def signup(request):
     form = signupform()
     if request.method == 'POST':
         form = signupform(request.POST)
         if form.is_valid():
             form.save(commit = True)
             return index(request)
         else:
             print("Error Form Invalid")
     return render(request, 'app2/signup.html',{'form':form})
