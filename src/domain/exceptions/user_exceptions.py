class UserNotFound(Exception):
    def __init__(self, message, errors=None):
        super(UserNotFound, self).__init__(message)
        self.errors = errors
        self.message = message

    def __str__(self):
        return 'user {0} not found'.format(self.message)


class PasswordNotCheck(Exception):
    def __init__(self, message='', errors=None):
        super(PasswordNotCheck, self).__init__(message)
        self.errors = errors

    def __str__(self):
        return 'user not found'
