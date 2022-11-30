from fastapi import Request

def is_json_request(request: Request) -> bool:
    headers = request.headers

    content_type = headers.get("Content-Type")

    if content_type and content_type == 'application/json':
        return True

    return False