from fastapi import FastAPI

app = FastAPI(
    title="Course25 API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to Course25 API"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }
