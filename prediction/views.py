import os
import pickle
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, PredictionForm

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, 'model', 'mail_model.pkl')
VECT_PATH = os.path.join(BASE_DIR, 'model', 'mail_vectorizer.pkl')

model = pickle.load(open(MODEL_PATH, 'rb'))
vectorizer = pickle.load(open(VECT_PATH, 'rb'))


def home(request):
    return render(request, 'prediction/index.html')


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Registration successful. Please login.")
        return redirect('login')
    return render(request, 'prediction/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('predict')
        messages.error(request, "Invalid username or password")
    return render(request, 'prediction/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

def about_view(request):
    return render(request, 'prediction/about.html')



@login_required

def predict_view(request):
    form = PredictionForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        text = form.cleaned_data['message']

        X = vectorizer.transform([text])
        prediction = model.predict(X)[0]

        if prediction == 0:
            result = "HAM"
        else:
            result = "SPAM"

        return render(
            request,
            'prediction/result.html',
            {
                'result': result,
                'text': text
            }
        )

    return render(request, 'prediction/predict.html', {'form': form})

 

@login_required
def result_view(request):
    context = {
        'label': request.session.get('label'),
        'text': request.session.get('text'),
        'spam_confidence': request.session.get('spam_confidence'),
        'ham_confidence': request.session.get('ham_confidence'),
    }

    if not context['label']:
        return redirect('predict')

    return render(request, 'prediction/result.html', context)