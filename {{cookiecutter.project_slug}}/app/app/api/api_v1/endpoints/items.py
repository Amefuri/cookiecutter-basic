from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.get("/test_items")
def testItems():
    return {"Test": "1234"}