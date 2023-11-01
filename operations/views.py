from django.shortcuts import render
from django.views.generic import View


class HelloWorldView(View):
    def get(self,request,*args,**kwargs):
        print("indise helloworld viw get method")
        return render(request,"helloworld.html")
    




class GoodMorningView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"gm.html")
    


class GoodAfternoonView(View):

    def get(self,request,*args,**kwargs):
        return render(request,"an.html")
    




class AdditionView(View):

    def get(self,request,*args,**kwargs):

        return render(request,"add.html")
    
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        print(result)


        return render(request,"add.html",{"out":result})
    



class FactorialView(View):

    def get(self,request,*args, **kwargs):
        return render(request,"fact.html")
    
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")

        fact=1

        for i in range(1,int(n)+1):
            fact=fact*i
        print(fact)
        return render(request,"fact.html")
    



# leapyerView

# oddevenView

# primenumberview

# django cbv 