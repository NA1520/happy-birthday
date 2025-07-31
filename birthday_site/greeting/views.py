from django.shortcuts import render
from datetime import date

def birthday_page(request):
    today = date.today()
    birthday =  date(2025, 8, 4)

    if today == birthday:
        context = {
            'name': 'Айбийке',
            'message': 'Желаю тебе счастья, любви, вдохновения и тепла каждый день! 🌸',
            'today': today,
        }
        return render(request, 'greeting/birthday.html', context)
    else:
        return render(request, 'greeting/wait.html', {'days_left': (birthday - today).days})
