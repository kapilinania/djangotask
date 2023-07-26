from django.shortcuts import render


def calculator(request):
    c=''
    try:
        if request.method == "POST":
            pass
            data1 = eval(request.POST.get('num1'))
            data2 = eval(request.POST.get('num2'))
            opr = request.POST.get('oper')
            if opr == "+":
                c = data1+data2
            elif opr == "-":
                c = data1-data2
            elif opr == "*":
                c = data1 - data2
            elif opr == "/":
                c = data1/data2

    except:
        c= "Invalid Operation ...."
    print(c)
    return render(request, "index.html",{'c':c})

def evenoddprogram(request):
    c = ''

    if request.method == "POST":
        if request.POST.get('num1') =="":
            return render(request, "evenodd.html", {'error': True})

        data1 = eval(request.POST.get('num1'))

        if data1 % 2 == 0:
            c = "even"
        else:
            c = "odd"

    print(c)
    return render(request, "evenodd.html", {'c': c})

def marksheet(request):
    total=''
    percent=''
    divison=''

    try:
        if request.method == "POST":
            hindival = eval(request.POST.get('hindi'))
            engval = eval(request.POST.get('eng'))
            mathsval = eval(request.POST.get('maths'))
            scival = eval(request.POST.get('sci'))
            sstval = eval(request.POST.get('sst'))

            total = hindival+engval+mathsval+scival+sstval
            percent = total/5
            print(total)
            print(percent)

            if percent >=90:
                divison = 'first division'
            elif percent >=60:
                divison = 'first division'
            elif percent >=33:
                divison = 'Pass'
            elif percent <=33:
                divison = 'Fail'


    except:
        c = "Enter a Valid Number"
        print(c)

    return render(request, "marksheet.html", {'total':total, 'percent':percent, 'divison':divison})

def website(request):
    return render(request, "web.html")
