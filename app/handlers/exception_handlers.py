from app.templates import templates

async def exception_handler_for_404(request, exc):
    return templates.TemplateResponse(
        "index.html", context={"request": request}
    )
    