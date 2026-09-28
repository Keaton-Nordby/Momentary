from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select
from app.images import imagekit
import shutil
import os
import uuid
import tempfile


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield



app = FastAPI(lifespan=lifespan)




@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    caption: str = Form(""),
    session: AsyncSession = Depends(get_async_session)
):
    """
    Upload an image to ImageKit and save its metadata to PostgreSQL.

    The uploaded file is temporarily stored on disk while it is sent
    to ImageKit. The temporary file is always removed when the request
    finishes, even if an error occurs.
    """

    temp_file_path = None

    try:
        # Validate that a file was actually provided.
        if not file.filename:
            raise HTTPException(
                status_code=400,
                detail="A file is required."
            )

        # Only allow supported image formats.
        allowed_types = {
            "image/jpeg",
            "image/png",
            "image/webp",
            "image/gif"
        }

        if file.content_type not in allowed_types:
            raise HTTPException(
                status_code=400,
                detail="Unsupported file type. Please upload a JPEG, PNG, WebP, or GIF."
            )

        # Copy the uploaded file into a temporary file.
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=os.path.splitext(file.filename)[1]
        ) as temp_file:
            temp_file_path = temp_file.name
            shutil.copyfileobj(file.file, temp_file)

        # Reject empty files.
        if os.path.getsize(temp_file_path) == 0:
            raise HTTPException(
                status_code=400,
                detail="The uploaded file is empty."
            )

        # Limit uploads to 10 MB.
        if os.path.getsize(temp_file_path) > 10 * 1024 * 1024:
            raise HTTPException(
                status_code=400,
                detail="File size cannot exceed 10 MB."
            )

        # Upload the temporary file to ImageKit.
        with open(temp_file_path, "rb") as temp_file:
            upload_result = imagekit.files.upload(
                file=temp_file,
                file_name=file.filename,
                tags=["backend-upload"]
            )

        # Save the ImageKit metadata in PostgreSQL.
        post = Post(
            caption=caption,
            url=upload_result.url,
            file_type="image",
            file_name=upload_result.name
        )

        try:
            session.add(post)
            await session.commit()
            await session.refresh(post)
        except Exception:
            await session.rollback()
            raise

        return post

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="File upload failed."
        )

    finally:
        # Always remove the temporary file after the request.
        if temp_file_path and os.path.exists(temp_file_path):
            os.unlink(temp_file_path)

        # Close FastAPI's uploaded file handle.
        file.file.close()



@app.get("/feed")
async def get_feed(
    session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]
    
    
    posts_data = []
    for post in posts:
        posts_data.append(
            {
                "id": str(post.id),
                "caption": post.caption ,
                "url": post.url,
                "file_type": post.file_type,
                "file_name": post.file_name,
                "created_at": post.created_at.isoformat()
            }
        )
        
    return {"posts": posts_data}