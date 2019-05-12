from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html')


def calc(request):
    task = request.POST.get('task')
    try:
        number = float(task)
        context = {
            'number': number,
        }
        return render(request, 'app/result.html', context)
    except:
        return render(request, 'app/error.html')
