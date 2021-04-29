from ..schemas import Login, Tokens


def post_login(
    refresh: Login
) -> Tokens:
    return Tokens(**{
        'accessToken': 'access',
        'refreshToken': 'refresh'
    })
