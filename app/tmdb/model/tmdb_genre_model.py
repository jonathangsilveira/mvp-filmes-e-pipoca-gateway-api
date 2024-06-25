from pydantic import BaseModel

class TMDBGenreModel(BaseModel):
    """
    Modelo representando o gênero de determinado filme.
    """
    id: int
    name: str