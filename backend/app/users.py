import uuid, os
from dotenv import load_dotenv
from typing import Optional
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin, models
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy
)
from fastapi_users.db import SQLAlchemyUserDatabase
from app.db import User, get_user_db


load_dotenv(override=True)


JWT_SECRET = os.getenv("JWT_SECRET")

if not JWT_SECRET:
    raise RuntimeError("JWT_SECRET is not set")

class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = JWT_SECRET
    verification_token_secret = JWT_SECRET
    
    async def on_after_register(self, user, request = None):
        print(f"User {user.id} has registered.")
        
    async def on_after_forgot_password(self, user, token, request = None):
        print(f"User {user.id} has forgot their password. Reset token: {token}")
        
    async def on_after_request_verify(self, user, token, request = None):
        print(f"Verification requested for user {user.id}. Verification token: {token}")
        
        
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")   
        
async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)
    
    
def get_jwt_strategy():
    return JWTStrategy(secret=JWT_SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy
)

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])
current_active_user = fastapi_users.current_user(active=True)