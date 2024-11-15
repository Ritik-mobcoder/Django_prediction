from django.http import JsonResponse
import json
import pickle
import numpy as np
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def logistic_view(request):
    return render(request, 'logistic.html')

def regression_view(request):
    return render(request, 'regression.html')


@csrf_exempt
def titanic(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            pclass = body.get("pclass")
            sex = body.get("sex")
            age = body.get("age")
            sibsp = body.get("sibsp")
            parch = body.get("parch")
            fare = body.get("fare")
            input_data = np.array([[pclass, sex, age, sibsp, parch, fare]])
            model_path = "/home/mobcoder/ritik/DataScience/Django_prediction/log_linear/log_reg.pkl"
            with open(model_path, "rb") as f:
                model = pickle.load(f)
            prediction = model.predict(input_data)
            response_data = {"result": prediction.tolist()}
            return JsonResponse(response_data, status=200)
        
        except Exception as e:
            error_message = str(e)
            response_data = {"error": error_message}
            return JsonResponse(response_data, status=400)
    
    
# @csrf_exempt
# def expirence(request):
#     if request.method == "POST":
#         try:
#             body = json.loads(request.body)
#             expirence = body.get("expirence")
#             # expirence = int(expirence)   
#             input_data = np.array([[expirence]])
#             model_path = "/home/mobcoder/ritik/DataScience/Django_prediction/log_linear/model copy.pkl"
#             with open(model_path, "rb") as f:
#                 model = pickle.load(f)
#             prediction = model.predict(input_data)
#             response_data = {"result": prediction.tolist()}
#             return JsonResponse(response_data, status=200)
        
#         except Exception as e:
#             error_message = str(e)
#             response_data = {"error": error_message}
#             return JsonResponse(response_data, status=400)
    
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import numpy as np
import pickle

@csrf_exempt
def expirence(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            experience = body.get("experience")
            if experience is None:
                raise ValueError("Experience field is required.")

            # Prepare the input data for the model
            input_data = np.array([[experience]])

            # Load the trained model
            model_path = "/home/mobcoder/ritik/DataScience/Django_prediction/log_linear/model copy.pkl"  # Ensure the model.pkl file is in the correct directory
            with open(model_path, "rb") as f:
                model = pickle.load(f)

            # Make the prediction
            prediction = model.predict(input_data)

            # Return the prediction in JSON format
            response_data = {"prediction_salary": prediction.tolist()}
            return JsonResponse(response_data, status=200)

        except Exception as e:
            # Handle errors and return an error message
            error_message = str(e)
            response_data = {"error": error_message}
            return JsonResponse(response_data, status=400)

    # If the method is not POST, return a 405 Method Not Allowed
    return JsonResponse({"error": "Method not allowed"}, status=405)
