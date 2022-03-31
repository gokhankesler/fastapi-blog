from fastapi import FastAPI
from .schemas import Blog
from .models import Base
from .database import engine


app = FastAPI()


Base.metadata.create_all(engine)


@app.post('/blog')
def create(request: Blog):
    return {
        'title': request.title,
        'body': request.title
    }
