from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.schemas import UserCreate, UserRead ,Token
from app.models import User
from app.database import get_db
from app.core.security import hash_password, verify_password, create_access_token,verify_access_token
from app.rate_limit import check_rate_limit
from fastapi import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/users", tags=["users"])

#signup
@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    # optional rate limiting
    await check_rate_limit(user.email)

    # check if user exists using ORM select
    result = await db.execute(select(User).where(User.email == user.email))
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # hash password and create new user
    hashed_pw = hash_password(user.password)
    new_user = User(email=user.email, hashed_password=hashed_pw)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    return new_user

#login

oauth2_scheme =OAuth2PasswordBearer(tokenUrl="/users/login")

@router.post("/login",response_model=Token)
async def login(from_data: OAuth2PasswordRequestForm = Depends(), db:AsyncSession = Depends(get_db)):
    result = await db.execute(select(User)where(User.email == from_data.username))
    user = result.scalar_one_or_none()

    if not user or not verify_password(from_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub":user.email})
    return{"access_token": access_token, "token_type":"bearer"}


#Get current user
@router.get("/me", response_model=UserRead)
async def get_me(token: str =Depends(oauth2_scheme),db: AsyncSession = Depends(get_db)):
    payload = verify_access_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    
    result = await db.execute(select(User).where(User.email==payload["sub"]))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user