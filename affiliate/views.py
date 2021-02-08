from django.shortcuts import render

# Create your views here.
def affiliate(request):
    return render(request,'affiliate.html')

def menswear(request):
    return render(request,'menswear.html')
    # return HttpResponse("Mens wear")

def womens(request):
    return render(request,'womens.html')   

def grocerry(request):
    return render(request,'grocerry.html')    

def mobile(request):
    return render(request,'mobile.html')    

def electronic(request):
    return render(request,'electronic.html')    

def cosmetics(request):
    return render(request,'cosmetics.html')    

def homeappliance(request):
    return render(request,'homeappliance.html')  

def interior(request):
    return render(request,'interior.html')   
     
def sports(request):
    return render(request,'sports.html')    

def gym(request):
    return render(request,'gym.html')    
