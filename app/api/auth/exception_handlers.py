from starlette.responses import RedirectResponse
from fastapi import status
from fastapi_jwt_auth.exceptions import AuthJWTException
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.utils.detect_json_request import is_json_request


def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    if (is_json_request(request)):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"detail": exc.message})
    
    return RedirectResponse(url="/signin")
    
