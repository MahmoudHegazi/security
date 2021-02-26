# using this will allow u to define more than one premssion not repeat the @requires_auth

def get_token_auth_header():
    if 'Authorization' not in request.headers:
        abort(401)
    auth_header = request.headers['Authorization']
    header_parts = auth_header.split(' ')
    if len(header_parts) != 2:
        abort(401)
    elif header_parts[0].lower() != 'bearer':
        abort(401)
    token = header_parts[1]
    return token
def check_permissions(permission, payload):
    if 'permissions' not in payload:
                        raise AuthError({
                            'code': 'invalid_claims',
                            'description': 'Permissions not included in JWT.'
                        }, 400)

# my update
    if ',' not in permission:
        if permission not in payload['permissions']:
            raise AuthError({
                'code': 'unauthorized',
                'description': 'Permission not found.'
            }, 403)

    else:
        pemssions_list = permission.split(',')
        for pre in pemssions_list:
            if pre not in payload['permissions']:
                if permission not in payload['permissions']:
                    raise AuthError({
                        'code': 'unauthorized',
                        'description': 'Permission not found.'
                    }, 403)
# my update end
    return True

def requires_auth(permissions=''):
    def requires_auth_decroater(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            jwt = get_token_auth_header()
            try:
                payload = verify_decode_jwt(jwt)
            except:
                abort(401)
            check_permissions(permissions, payload)
            return f(payload, *args, **kwargs)
        return wrapper
    return requires_auth_decroater
