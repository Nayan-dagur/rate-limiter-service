from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

router = APIRouter(prefix="/api/v1", tags=["Protected Resources"])

class AnalysisRequest(BaseModel):
    user_id: str = Field(..., description="Unique client identifier")
    payload: str = Field(..., min_length=3, max_length=200, description="Task data string")

@router.get("/health")
async def health_check():
    """Public health check endpoint."""
    return {"status": "healthy", "service": "online"}

@router.post("/process-data", status_code=status.HTTP_200_OK)
async def process_data(data: AnalysisRequest):
    """A resource-intensive simulation endpoint."""
    return {
        "status": "success",
        "processed_by": data.user_id,
        "payload_length": len(data.payload),
        "message": "Data processed successfully."
    }
