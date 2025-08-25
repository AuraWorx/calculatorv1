"""Main FastAPI application for Calculator API."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Union

app = FastAPI(
    title="Calculator API",
    description="A simple calculator API with basic arithmetic operations",
    version="1.0.0"
)


class CalculationRequest(BaseModel):
    """Request model for calculation operations."""
    a: Union[int, float]
    b: Union[int, float]
    operation: str


class CalculationResponse(BaseModel):
    """Response model for calculation results."""
    result: Union[int, float]
    operation: str
    a: Union[int, float]
    b: Union[int, float]


def calculate(a: Union[int, float], b: Union[int, float], operation: str) -> Union[int, float]:
    """Perform basic arithmetic calculations."""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    else:
        raise ValueError(f"Unsupported operation: {operation}")


@app.get("/")
async def root():
    """Root endpoint returning API information."""
    return {
        "message": "Calculator API",
        "version": "1.0.0",
        "endpoints": ["/calculate", "/health"]
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.post("/calculate", response_model=CalculationResponse)
async def perform_calculation(request: CalculationRequest):
    """Perform arithmetic calculation based on request."""
    try:
        result = calculate(request.a, request.b, request.operation)
        return CalculationResponse(
            result=result,
            operation=request.operation,
            a=request.a,
            b=request.b
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
