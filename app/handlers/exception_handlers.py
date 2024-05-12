from fastapi import Request, Response, status

from app.templates import templates


async def exception_handler_for_404(request: Request, exc: Exception) -> Response:
    return templates.TemplateResponse(
        "not_found.html",
        context={"request": request},
        status_code=status.HTTP_404_NOT_FOUND,
    )
