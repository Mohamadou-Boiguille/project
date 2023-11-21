/session/
    - recupere le cookie
/whoami/
    - recupere ton profil
/logout/
    - deconnexion
/tournaments/
    - liste des tournois disponible
/login/
    - request POST
    headers:
        - Content-Type = application/json
        - X-CSRFToken = (token contenu dans le cookie)
        - body = {"username", "votre username", "password", "votre mot de passe"}
/signin/
    - request POST
    headers:
        - Content-Type = application/json
        - X-CSRFToken = (token contenu dans le cookie)
        - body = {"username", "votre username", "password", "votre mot de passe"}
