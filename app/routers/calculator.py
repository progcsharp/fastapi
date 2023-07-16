from fastapi import APIRouter, Request

from datetime import date as d

from app.db.handlers.get import get_rate


router_calculator = APIRouter(prefix="/calculator", responses={404: {"description": "Not found"}})


@router_calculator.get("/")
async def calculator(price: float, date: d, cargo_type: str):
    rate = await get_rate(date, cargo_type)
    return {"price": price*rate.rate}
