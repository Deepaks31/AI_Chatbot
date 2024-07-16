from django.shortcuts import render,redirect
from django.http import JsonResponse

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = 'hi this is my response'
        return JsonResponse ({'message': message, 'response':response})
    return render(request,'chatbot.html')