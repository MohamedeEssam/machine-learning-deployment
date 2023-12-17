from django.shortcuts import render
from joblib import load
model = load('./savedModels/model.joblib')
# Create your views here.
def predictor(request):
    if request.method == 'POST':
        passenger_count = int(request.POST['passenger_count'])
        hour = int(request.POST['hour'])
        month = int(request.POST['month'])
        weekday = int(request.POST['weekday'])
        year = int(request.POST['year'])
        distance = int(request.POST['distance'])
        y_pred = model.predict([[passenger_count, hour, month, weekday, year, distance]])
        return render(request, 'main.html', {'result':y_pred})
    return render(request, 'main.html')

