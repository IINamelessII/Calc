from django.shortcuts import render
from app.entities import CalcRequest


def index(request):
    return render(request, 'app/index.html')


def calc(request):
    task = request.POST.get('task')
    try:
        calc_request = CalcRequest(task)
        context = {
            'number': calc_request.calc(),
        }
        return render(request, 'app/result.html', context)
    except:
        return render(request, 'app/error.html')
