from app import config
from fastapi.security import OAuth2PasswordBearer
import datetime
from typing import Optional
from fastapi import HTTPException, Depends, status
from jose import jwt, JWTError
from pydantic import ValidationError
from datetime import datetime, timedelta

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class Authentication(object):

    def generate_magic_link(self, email, url):
        payload = {
            "email": email,
            "exp": datetime.utcnow() + config.MAGIC_LINK_EXPIRE_MINUTES
        }
        token = jwt.encode(payload, config.JWT_SECRET_KEY, algorithm=config.ALGORITHM)
        magic_link = f"{url}/auth?token={token}"
        return magic_link

    def create_access_token(self, data: dict):
        to_encode = data.copy()
        to_encode.update({"exp": jwt.datetime.utcnow() + jwt.timedelta(minutes=int(config.ACCESS_TOKEN_EXPIRE_MINUTES))})
        encoded_jwt = jwt.encode(to_encode, config.JWT_SECRET_KEY, algorithm=config.ALGORITHM)
        return encoded_jwt

    def create_refresh_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta is None:
            expires_delta = timedelta(days=int(config.REFRESH_TOKEN_EXPIRE_DAYS))
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, config.JWT_SECRET_KEY, algorithm=config.ALGORITHM)
        return encoded_jwt

    def validate_refresh_token(self, refresh_token: str):
        try:
            payload = jwt.decode(refresh_token, config.JWT_SECRET_KEY, algorithms=[config.ALGORITHM])
            id: str = payload.get("sub")
            if id is None:
                raise HTTPException(status_code=400, detail="Invalid refresh token")
            return id
        except JWTError:
            raise HTTPException(status_code=403, detail="Could not validate credentials")


    def validate_token(self, token: str = Depends(oauth2_scheme)):
        try:
            # Decode the token
            payload = jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.ALGORITHM])

            id: str = payload.get("sub")
            if id is None:
                raise HTTPException(status_code=400, detail="Invalid token payload")

            return id

        except JWTError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except ValidationError as e:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Token validation error"
            )

    def validate_token_bool(self, token: str = Depends(oauth2_scheme)):
        try:
            # Decode the token
            payload = jwt.decode(token, config.JWT_SECRET_KEY, algorithms=[config.ALGORITHM])

            id: str = payload.get("sub")
            if id is None:
                return False

            return True

        except JWTError as e:
            return False
        except ValidationError as e:
            return False
