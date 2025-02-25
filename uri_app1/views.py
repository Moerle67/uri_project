from django.shortcuts import render

# Create your views here.

def start(request):
    name = "Hr. Mörl"
    titel = "Ausbilder"
    title = "Irgend etwas anderes"
    content = {
        'name': name,
        'titel': titel,
        'title': title,
    }
    return render(request, 'uri_app1/seite1.html', content)
