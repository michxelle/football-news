from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406419594',
        'name': 'Laudya Michelle Alexandra',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)