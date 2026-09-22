from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse


app = FastAPI()

text_posts = {
    1: {
        "title": "New Post",
        "content": "One test post"
    },
    2: {
        "title": "Learning FastAPI",
        "content": "Today I started learning how to build APIs with FastAPI."
    },
    3: {
        "title": "Python Project",
        "content": "I am building a small backend project to practice Python and REST APIs."
    },
    4: {
        "title": "Weekend Plans",
        "content": "Going to the gym and working on my coding projects this weekend."
    },
    5: {
        "title": "API Testing",
        "content": "Testing GET, POST, PUT, and DELETE endpoints to understand how APIs work."
    },
    6: {
        "title": "Backend Development",
        "content": "FastAPI makes it pretty easy to create endpoints and automatically generate API documentation."
    },
    7: {
        "title": "Programming Goals",
        "content": "I want to become stronger at Python, backend development, and system design."
    },
    8: {
        "title": "First API",
        "content": "This is one of my first APIs, and I am experimenting with different endpoints."
    },
}


@app.get("/posts")

def get_all_posts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts{id}")
def get_post(id: int) -> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)


@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post


