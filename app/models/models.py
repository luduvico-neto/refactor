from pydantic import BaseModel
from sentence_transformers.util.tensor import Tensor


class Row(BaseModel):
    neighborhood: str
    city: str
    state: str
    average_price: float
    ad_quantity: int
    days_in_market: int
    embedding: Tensor | None = None

    model_config = {
        "arbitrary_types_allowed": True,
    }


class DataFrame(BaseModel):
    data: list[Row]
