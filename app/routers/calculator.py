from fastapi import APIRouter, Request, HTTPException

from datetime import date as d

from app.db.handlers.get import get_rate


router_calculator = APIRouter(prefix="/calculator", responses={404: {"description": "Not found"}})


@router_calculator.get("/")
async def calculator(price: float, cargo_type: str, date: d = d.today()):
    try:
        rate = await get_rate(date, cargo_type.lower())
        return {"price": price*rate.rate}
    except:
        raise HTTPException(status_code=404, detail="Rate not found")
