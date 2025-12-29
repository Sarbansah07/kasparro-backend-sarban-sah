from pydantic import BaseModel

class UnifiedSchema(BaseModel):
    source: str
    some_string: str
    some_integer: int
