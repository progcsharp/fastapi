from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.routers import rate
from app.routers import calculator

app = FastAPI()

app.include_router(rate.router_rate)
app.include_router(calculator.router_calculator)


register_tortoise(
    app,
    db_url="sqlite://database",
    modules={"models": ["app.db.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
