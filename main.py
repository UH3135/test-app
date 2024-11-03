from chain import chain
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from langserve import add_routes

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/chat/playground")
add_routes(app, chain, path="/chat")

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="localhost", port=8000)
    # http://localhost:8000/chat/playground/
    # 위 링크에 접속