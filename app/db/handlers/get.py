from app.db.models import Rate

from datetime import date as d


async def get_rate(date: d, cargo_type: str):
    rate = await Rate.filter(date=date, cargo_type=cargo_type).first()
    return rate
