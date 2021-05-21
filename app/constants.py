class Constants:

    class Users:
        USER_ALREADY_EXISTS_MSG = 'User with login "{login}" already exists'
        USER_DO_NOT_EXISTS_MSG = 'User with id "{id}" do not exists'
        ROLE_DOES_NOT_EXIST_MSG = 'Role with code "{code}" does not exist'

    class Roles:
        ROLE_ALREADY_EXISTS_MSG = 'Role with code "{code}" already exists'
        ROLE_DOES_NOT_EXIST_MSG = 'Role with code "{code}" does not exist'
        ROLE_IS_NOT_EMPTY_MSG = 'There is one or more users for role with code "{code}"'
        PERMISSION_DOES_NOT_EXIST_MSG = 'Permission with code "{code}" does not exist'

    class Auth:
        WRONG_USER_OR_PASSWORD_MSG = 'Wrong user/password or user is blocked or deleted'
        USER_IS_DELETED_OR_BLOCKED_MSG = 'User is deleted or blocked'

    class Token:
        LOGIN_URL = 'api/v1/auth/login'
        INVALID_SIGNATURE_MSG = 'Invalid token signature'
        EXPIRED_SIGNATURE_MSG = 'Token had been expired'
        INVALID_TOKEN_MSG = 'Invalid token'
        WRONG_TOKEN_TYPE_MSG = 'Wrong token type'
        FORBIDDEN_MSG = 'You don\t have permissions to do that'

    class Patients:
        PATIENT_DOES_NOT_EXIST_MSP = 'Patient with id "{id}" does not exist'
