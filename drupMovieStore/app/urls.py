from django.urls import path, include
from app.views import users, movies
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter 


# app_name = 'app'
router = DefaultRouter()

# crud models
router.register('movies', movies.MovieView)


urlpatterns = [
    path('', include(router.urls)),
    # generate token
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    # account registration
    path('account/registration/', users.create_user),
    path('account/authentication/', users.authenticate_user),
    path('account/logout/', users.close_session),
    path('init', users.init, name='init'),
    
    
    path('home', movies.show, name='home'),
    path('movies/delete/<int:pk>', movies.delete), 
    path('movies/update/<int:pk>', movies.edit), 
]