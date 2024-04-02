from django.shortcuts import render
from .utils import HousePricePredictor
# Create your views here.

def predict(request):
    if request.method == 'POST':
        location = request.POST['location']
        sqft = int(request.POST['sqft'])
        bath = int(request.POST['bath'])
        bhk = int(request.POST['bhk'])

        predictor = HousePricePredictor()

        try:
            predicted_price = predictor.predict_price(location, sqft, bhk, bath)
            return render(request, 'prediction.html', {'predicted_price': predicted_price})
        except Exception as e:  # Catch any unexpected errors
            error_message = f"An error occurred: {str(e)}"
        return render(request, 'prediction.html', {'error_message': error_message})
    else:
        return render(request, 'prediction.html')
