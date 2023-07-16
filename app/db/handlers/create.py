from app.db.models import Rate


async def create_rate(data):
    try:
        await Rate(date=data["date"], cargo_type=data["cargo_type"], rate=data["rate"]).save()
        return True
    except:
        return False