from fastapi import Header, HTTPException
from app.core.config import settings
from app.core.security import verify_token

def get_api_key(api_key:str=Header(...)):
    if api_key != settings.API_KEY:
        raise HTTPException(
            status_code=403,
            detail="Invalid API Key"
        )
    
    
def get_current_user(token: str = Header(...)):
    try:
        payload = verify_token(token)
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        return {"user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials") from e    
    
   