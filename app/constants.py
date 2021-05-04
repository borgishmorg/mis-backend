class Constants:

    class Users:
        USER_ALREDY_EXISTS_MSG = 'User with login "{login}" alredy exists'
        USER_DO_NOT_EXISTS_MSG = 'User with id "{id}" do not exists'

    class Auth:
        WRONG_USER_OR_PASSWORD_MSG = 'Wrong user/password'

    class Token:
        LOGIN_URL = 'api/v1/auth/login'
        INVALID_SIGNATURE_MSG = 'Invalid token signature'
        EXPIRED_SIGNATURE_MSG = 'Token had been expired'
        INVALID_TOKEN_MSG = 'Invalid token'
        WRONG_TOKEN_TYPE_MSG = 'Wrong token type'
        FORBIDDEN_MSG = 'You don\t have permissions to do that'
