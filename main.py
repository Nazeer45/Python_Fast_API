from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "About page"}

@app.get("/blog/{id}")
def blog(id: int):
    return {"id": id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1', '2'}}

@app.get('/blog')
def index(limit: int = 10, published: bool = False, sort: Optional[str] = None):
    # only get {limit} number of blogs
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    
@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}'}