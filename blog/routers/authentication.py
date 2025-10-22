from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from blog import database, models, JWTtoken
from blog.hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login', status_code=status.HTTP_200_OK)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials - email does not exist!')
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentials - Password does not match!')
    
    #generating JWT token
    access_token = JWTtoken.create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}