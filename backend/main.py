from fastapi import FastAPI

app = FastAPI(
    title="AgentOS",
    version="0.1.0",
    description="Enterprise Multi-Agent AI Workspace",
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to AgentOS 🚀",
        "status": "running",
    }
