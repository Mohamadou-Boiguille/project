import json
from logging import log

from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from accounts.models import CustomUser


# Create your views here.

@require_POST
def login_view(request):
    if request.user.is_authenticated:
        return JsonResponse({'detail': 'You\'re logged in.'}, status=400)
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    print("this is the request =>", username, password)
    if username is None or password is None:
        return JsonResponse({'detail': 'Please provide username and password.'}, status=400)

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({'detail': 'Invalid credentials.'}, status=400)

    login(request, user)
    return JsonResponse({'detail': 'Successfully logged in.'})


def logout_view(request):
    print("this is the request =>", request)
    if not request.user.is_authenticated:
        return JsonResponse({'detail': 'You\'re not logged in.'}, status=400)

    logout(request)
    return JsonResponse({'detail': 'Successfully logged out.'})


@ensure_csrf_cookie
def session_view(request):
    print("this is the request =>", request)
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    return JsonResponse({'isAuthenticated': True})

@ensure_csrf_cookie
def whoami_view(request):
    print("this is the request =>", request)
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})

    return JsonResponse({'username': request.user.username, 'victories': request.user.victories, 'defeats': request.user.defeats, 'Tplayed': request.user.tournamentsPlayed, 'Twon': request.user.tournamentsWon})

def signin_view(request):
    if request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': True})
    data = json.loads(request.body)
    newuser = data.get('username')
    newpass = data.get('password')

    if newuser is None or newpass is None:
        return JsonResponse({'detail': 'Please provide username and password.'}, status=400)

    user, created = CustomUser.objects.get_or_create(username=newuser, password=newpass)

    if created:
        user.set_password(newpass)
        user.save()
    else:
        return JsonResponse({'detail': 'User with this username already exists.'}, status=400)


    print("this is the request =>", request, "<==>", data.get('username'))
    user = authenticate(username=newuser, password=newpass)
    if user is not None:
        login(request, user)
        print("user", user)
        return JsonResponse({'detail': 'Successfully signed in.'})
    else:
        print("failed")
        return JsonResponse({'detail': 'Failed to sign in.'}, status=400)

@ensure_csrf_cookie
def tournaments_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'isAuthenticated': False})
    return JsonResponse(dummy_tournament)

dummy_tournament = {
  "tournament_name": "Pong Tournament 2023",
  "number_of_players": 8,
  "players": [
    {
      "player_name": "Alice",
      "victories": 20,
      "defeats": 12,
      "tournaments_won": 0
    },
    {
      "player_name": "Bob",
      "victories": 15,
      "defeats": 7,
      "tournaments_won": 2
    },
    {
      "player_name": "Charlie",
      "victories": 20,
      "defeats": 12,
      "tournaments_won": 1
    },
    {
      "player_name": "David",
      "victories": 18,
      "defeats": 10,
      "tournaments_won": 3
    },
    {
      "player_name": "Eva",
      "victories": 22,
      "defeats": 5,
      "tournaments_won": 2
    },
    {
      "player_name": "Frank",
      "victories": 25,
      "defeats": 8,
      "tournaments_won": 1
    },
    {
      "player_name": "Grace",
      "victories": 19,
      "defeats": 11,
      "tournaments_won": 2
    },
    {
      "player_name": "Harry",
      "victories": 17,
      "defeats": 9,
      "tournaments_won": 1
    }
  ]
}

