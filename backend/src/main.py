from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from src.views.auth_routes import auth
from src.views.request_routes import request

app.include_router(auth)
app.include_router(request)

@app.get("/")
async def root():
    return {"message": "Sistema funcionando!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Para rodar o código, executar no terminal: uvicorn src.main:app --reload