def add_claims_to_access_token(user):
    return {'role': user.role.name}


def user_identity_lookup(user):
    return user.login
