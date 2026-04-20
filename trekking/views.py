#from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

#def trekking_list(request):
#    return HttpResponse("MyTrekking is alive 🚶‍♂️⛰️")

#from django.shortcuts import render
#from .models import YourTrekking

#def trekking_list(request):
#    trekkings = YourTrekking.objects.all().order_by('-trek_date')
#    return render(request, 'trekking/list.html', {'trekkings': trekkings})

from django.http import HttpResponse

def trekking_list(request):
    html_content = """
    <html>
        <head>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f0f2f5;
                    font-family: sans-serif;
                }
                h1 {
                    font-size: 2.5rem; /* Makes it big */
                    color: #2e7d32;   /* A nice trekking green */
                    text-align: center;
                    padding: 20px;
                }
            </style>
        </head>
        <body>
            <h1>MyTrekking is alive 🚶‍♂️⛰️</h1>
        </body>
    </html>
    """
    return HttpResponse(html_content)
