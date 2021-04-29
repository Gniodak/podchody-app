from django.shortcuts import render


def sound(request):
    return render(request, 'sound.html')


def riddle(request):
    return render(request, 'riddle.html')


def blank(request):
    return render(request, 'blank.html')
