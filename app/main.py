from fastapi import FastAPI
from app.api.routes import movie_routes
from app.infrastructure.database import init_db
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Cine Reservation Management System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    init_db()

app.include_router(movie_routes.router)

@app.get("/health")
@app.get("/")
def health():
    return {"status": "ok"}
