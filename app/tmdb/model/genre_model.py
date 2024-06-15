from pydantic import BaseModel

class GenreModel(BaseModel):
    """
    Modelo representando o gênero de determinado filme.
    """
    id: int
    name: str