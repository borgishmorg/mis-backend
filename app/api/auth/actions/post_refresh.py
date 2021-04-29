from ..schemas import Refresh, Tokens


def post_refresh(
    refresh: Refresh
) -> Tokens:
    return Tokens(**{
        'accessToken': 'access',
        'refreshToken': 'refresh'
    })
