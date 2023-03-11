from datetime import datetime
from typing import Text, Optional
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()
posts = []


# Post Model
class Post(BaseModel):
    id: Optional[str]
    title: str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]
    is_published: bool = False


@app.get('/')
def read_root():
    return {"welcome": "welcome to my Api"}


@app.get('/posts')
def get_posts():
    return posts


@app.post('/posts', status_code=201)
def save_posts(post: Post, response: Response):
    post.id = str(uuid4())
    posts.append(post.dict())
    response.status_code = status.HTTP_201_CREATED
    return post


@app.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post["id"] == post_id:
            return post

    raise HTTPException(status_code=404, detail="Post not found")


@app.put('/posts/{post_id}')
def update_post(post_id: str, updatePost: Post):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts[index]["title"] = updatePost.title
            posts[index]["content"] = updatePost.content
            posts[index]["author"] = updatePost.author
            return {"message": "Post updated successfully"}

    raise HTTPException(status_code=404, detail="Post not found")


@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post["id"] == post_id:
            posts.pop(index)
            return {"message": "Post deleted successfully"}

    raise HTTPException(status_code=404, detail="Post not found")
