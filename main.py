from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()


@app.get('/blog')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the database.'}
    else:
        return {'data': f'{limit} total blogs from the database.'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'published'}


@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id: int, limit: int = 10):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}'}
