from fastapi import FastAPI

from src.conf import settings
from src.currency.routes import router as currency_router


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version=settings.version,
)

app.include_router(currency_router)
