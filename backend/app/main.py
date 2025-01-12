# backend/app/main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import httpx
from datetime import datetime

app = FastAPI(
    title="Hedge Fund Manager API",
    description="API for managing hedge fund portfolios and analytics",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """
    Root endpoint providing API status and information.
    """
    return {
        "status": "operational",
        "version": "1.0.0",
        "timestamp": datetime.utcnow().isoformat(),
        "endpoints": {
            "docs": "/docs",
            "health": "/health",
            "portfolio": "/portfolio"
        }
    }

@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring API status.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/portfolio")
async def get_portfolio(authorization: str = Depends(lambda x: x.headers.get("Authorization"))):
    """
    Retrieve portfolio information for the authenticated user.
    """
    if not authorization:
        raise HTTPException(status_code=401, detail="No authorization token provided")
    
    # Mock portfolio data for demonstration
    return {
        "status": "success",
        "data": {
            "portfolio_value": 1234567,
            "daily_return": 2.4,
            "monthly_return": 8.45,
            "risk_metrics": {
                "sharpe_ratio": 1.25,
                "volatility": 12.5,
                "beta": 0.85
            }
        }
    }