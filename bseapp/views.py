from django.shortcuts import render
from bseapp.models import user
from bsedata.bse import BSE
import re
# Create your views here.
b = BSE()


def getstprice(code):
    return b.getQuote(code)["currentValue"]


def index(request):
    return render(request, 'index.html')
def stprice(request):
    if request.method == 'POST': 
        name = request.POST.get('full-name')
        bsecode = request.POST.get('bsecode')
        try:
        
            currval = re.sub(r"()", " ", getstprice(bsecode),)
            compname = re.sub(r"()", " ", b.getQuote(bsecode)["companyName"],)
            wtdavg = re.sub(r"()", " ", b.getQuote(bsecode)["weightedAvgPrice"],)
            indus = re.sub(r"()", " ", b.getQuote(bsecode)["industry"],)
            yhigh = re.sub(r"()", " ", b.getQuote(bsecode)["52weekHigh"],)
            ylow = re.sub(r"()", " ", b.getQuote(bsecode)["52weekLow"],)
            marketcap = re.sub(r"()", " ", b.getQuote(bsecode)["marketCapFull"],)
            print(wtdavg)
        except:
            currval = 'invalid inputs'
            compname = 'invalid inputs'
            wtdavg = 'invalid inputs'
            indus = 'invalid inputs'
            yhigh = 'invalid inputs'
            ylow = 'invalid inputs'
            marketcap = 'invalid inputs'

        return render(request, "stprice.html", {'pername':name,'currval':currval,'compname':compname,'wtdavg':wtdavg,'indus':indus,'yhigh':yhigh,'ylow':ylow, 'marketcap':marketcap})
       
            
            
            

        userdata = user(name=name, bsecode=bsecode)
        userdata.save()
    return render(request, 'stprice.html')