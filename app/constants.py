class Constants:

    class Users:
        USER_ALREADY_EXISTS_MSG = 'User with login "{login}" already exists'
        USER_DO_NOT_EXISTS_MSG = 'User with id "{id}" do not exists'
        ROLE_DOES_NOT_EXIST_MSG = 'Role with code "{code}" does not exist'
        OLD_PASSWORD_DOES_NOT_SPECIFIED_MSG = 'Old password must be specified'
        WRONG_OLD_PASSWORD_MSG = 'Old password is wrong'
        NEW_PASSWORD_DOES_NOT_SPECIFIED_MSG = 'New password must be specified'

    class Roles:
        ROLE_ALREADY_EXISTS_MSG = 'Role with code "{code}" already exists'
        ROLE_DOES_NOT_EXIST_MSG = 'Role with code "{code}" does not exist'
        ROLE_IS_NOT_EMPTY_MSG = 'There is one or more users for role with code "{code}"'
        PERMISSION_DOES_NOT_EXIST_MSG = 'Permission with code "{code}" does not exist'

    class Auth:
        WRONG_USER_OR_PASSWORD_MSG = 'Wrong user/password'

    class Token:
        LOGIN_URL = 'api/v1/auth/login'
        INVALID_SIGNATURE_MSG = 'Invalid token signature'
        EXPIRED_SIGNATURE_MSG = 'Token had been expired'
        INVALID_TOKEN_MSG = 'Invalid token'
        WRONG_TOKEN_TYPE_MSG = 'Wrong token type'
        FORBIDDEN_MSG = 'You don\t have permissions to do that'
