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
    

class IndexView(View):

    def get(self,request,*args, **kwargs):
        return render(request,"index.html")
    

class LeapYearView(View):

    def get(self,request,*args, **kwargs):

        return render(request,"leapyear.html")
    
    def post(self,request,*args, **kwargs):
        year=int(request.POST.get("year"))
        

        if(year %100==0 and year%400==0 or year %100!=0 and year%4==0):
            result=f"{year} is a leap year"
        else:
            result=f"{year} is not a leap year"

        return render(request,"leapyear.html",{"out":result})




"""

p=total amount

n=anumber of months(year*12)

r= intrestperyear/12
i=r/100

"""

class EmiView(View):

    def get(self,request,*args,**kawargs):
        return render(request,"emi.html")
    
    def post(self,request,*args,**kwargs):
        p=int(request.POST.get("amount"))
        intrest_rate=int(request.POST.get("intrest"))
        tenure=int(request.POST.get("tenure"))
        n=tenure*12
        r=intrest_rate/12
        i=r/100
        print(i)

        #EMI=p*i(1+i)^n/(1+i)^n-1
        emi=p*i*(1+i)**n/((1+i)**n-1)
        emi=round(emi,0)
        total_payable_amount=emi*n
        total_interest_payable=total_payable_amount-p
        print(total_payable_amount)
        print(total_interest_payable)


        return render(request,"emi.html",{"emi":emi,
                                          "total_amount":total_payable_amount,
                                          "interest_amount":total_interest_payable
                                          }
                    )








