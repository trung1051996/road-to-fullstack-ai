from pydantic import BaseModel
class EmbeddedDocument(BaseModel):
    id: str
    content: str
    embedding: list[float]