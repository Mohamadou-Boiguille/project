/session/
    - request GET
    - recupere le cookie
/whoami/
    - request GET
    - recupere ton profil
/logout/
    - request GET
    - deconnexion
/tournaments/
    - request GET
    - liste des tournois disponible
/login/
    - request POST
    headers:
        - Content-Type = application/json
        - X-CSRFToken = (token contenu dans le cookie)
        - body = {"username": "votre username", "password": "votre mot de passe"}
/signin/
    - request POST
    headers:
        - Content-Type = application/json
        - X-CSRFToken = (token contenu dans le cookie)
        - body = {"username": "votre username", "password": "votre mot de passe"}
