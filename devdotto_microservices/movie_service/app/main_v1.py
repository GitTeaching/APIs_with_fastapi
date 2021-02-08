from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


# uvicorn app.main:app --reload
app = FastAPI()


# fake movies database
fake_movie_db = [
    {
        'name': 'Star Wars: Episode IX - The Rise of Skywalker',
        'plot': 'The surviving members of the resistance face the First Order once again.',
        'genres': ['Action', 'Adventure', 'Fantasy'],
        'casts': ['Daisy Ridley', 'Adam Driver']
    }
]

# Movie base model
class Movie(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts: List[str]


# API index endpoint
@app.get('/')
async def index():
    return {'Real':'Python'}


# API get_movie endpoint - GET
@app.get('/movies', response_model=List[Movie])
async def get_movies():
    return fake_movie_db


# API add_movie endpoint - POST
@app.post('/add_movie', status_code=201)
async def add_movie(payload: Movie):
    movie = payload.dict()
    fake_movie_db.append(movie)
    return {'id': len(fake_movie_db) - 1}


# API update_movie endpoint - PUT
@app.put('/update_movie/{id}')
async def update_movie(id: int, payload: Movie):
    movie = payload.dict()
    if 0 <= id <= len(fake_movie_db) :
        fake_movie_db[id] = movie
        return None
    raise HTTPException(status_code=404, detail='Movie with given id not found')


# API delete_movie endpoint - DELETE
@app.delete('/delete_movie/{id}')
async def delete_movie(id: int):
    if 0 <= id <= len(fake_movie_db) :
        del fake_movie_db[id]
        return None
    raise HTTPException(status_code=404, detail='Movie with given id not found')