from django.shortcuts import render

def process(request):
    if request.method == 'GET':
        template = 'process.html'
        context = {}

        return render(request, template, context)
