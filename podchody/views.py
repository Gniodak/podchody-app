from django.shortcuts import render


def sound(request):
    return render(request, 'sound.html')

def test(request):
    return render(request, 'test.html')

