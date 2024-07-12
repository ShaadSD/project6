from django.shortcuts import render
import datetime
def home(request):
    d={'author':'rakib','age': 5,'word':'my name is shaad','lst':["python","is","best"],'lenth':'21','birthday' : datetime.datetime.now(),'heading': 'Hello &lt;i>my&lt;/i> World!','courses':[
    {
        'id':1,
        'name': 'python',
        'fee': 5000
    },
    {
        'id':2,
        'name': 'Django',
        'fee': 10000
    },
    {
        'id':3,
        'name': 'C',
        'fee': 1000
    },
    ]
    
    }
    return render(request,'home.html',d)
