from fastapi import APIRouter, Request

from app.db.handlers.create import create_rate

router_rate = APIRouter(prefix="/rate", responses={404: {"description": "Not found"}})


@router_rate.post("/create")
async def rate_create(request: Request):
    request = await request.json()
    dates = request.keys()
    data = {}
    created = True
    for date in dates:
        for rate in request[date]:
            data["date"] = date
            data["cargo_type"] = rate["cargo_type"].lower()
            data["rate"] = rate["rate"]
            created = await create_rate(data)
    return {"created": created}
