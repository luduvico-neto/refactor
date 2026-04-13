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


class Column(BaseModel):
    name: str
    parser: str


class CreationMetadata(BaseModel):
    file_path: str
    sheet_name: str
    skip_rows: int
    skip_footer: int
    columns: list[Column]


class RetrievalMetadata(BaseModel):
    file_path: str
    sheet_name: str
    skip_rows: int
    skip_footer: int
    columns: list[Column]


class SheetMetadata(BaseModel):
    creation_metadata: CreationMetadata
