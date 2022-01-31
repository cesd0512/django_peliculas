#Django
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.shortcuts import render, redirect


@csrf_exempt
@api_view(['POST'])
def authenticate_user(request):
    """
    Return valid authentication.
    """
    try:
        name = request.data.get('username')
        password = request.data.get('pwd')
        user = authenticate(username=name, password=password)
        print(user)
        
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        user = model_to_dict(user)
        user.update({'token': token.key})
        request.session['auth'] = True
        return redirect('home')
    except Exception as e:
        print('error login ', e)
        return render(request, 'forms/login.html', {
            'message': 'Usuario o contraseña incorrecta'
        })
    

@csrf_exempt
@api_view(['POST']) 
def create_user(request):
    """This endpoint create user and return succesful creation
    """
    try:
        password = request.data.get('pwd')
        name = request.data.get('username')
        fname = request.data.get('first_name')
        lname = request.data.get('last_name')
        email = request.data.get('email')
        if not password or not name or not fname or not lname or not email:
            return render(request, 'forms/login.html', {
                'message': '¡Error! Campos vacios'
            }) 
        user = User.objects.create_user(
            username=name, password=password, first_name=fname, 
            last_name=lname, email=email)
        
        user.save()
        return render(request, 'forms/login.html', {
            'message': 'Usuario creado exitosamente'
        })  
   
    except Exception as inst:
        return render(request, 'forms/login.html', {
                'message': inst.args
            }) 
    

@csrf_exempt
@api_view(['GET']) 
def close_session(request):
    """ close session user
    """
    logout(request)
    request.session['auth'] = False
    return redirect('init')


def init(request):  
    return render(request, 'forms/login.html', {'message': ''})  

