from django.shortcuts import render,redirect
from django.http import JsonResponse
import openai 


openai_api_key ='sk-None-RDwDeqMV6mkjwefabTmYT3BlbkFJCWI5lG7TO5OIv3q2Cyo5'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt= message,
        max_tokens = 150,
        n=1,
        stop=None,
        tempreature = 0.7,
    )

    print(response)

    answer = response.choice[0].text.strip()
    return answer

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse ({'message': message, 'response':response})
    return render(request,'chatbot.html')