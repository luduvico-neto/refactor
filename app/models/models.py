from pydantic import BaseModel


class Row(BaseModel):
    neighborhood: str
    city: str
    state: str
    average_price: float
    ad_quantity: int
    days_in_market: int


class DataFrame(BaseModel):
    data: list[Row]
