from fastapi import FastAPI
app = FastAPI(title="cs_project API")

@app.get("/health")
def health():
    return {"status": "ok"}
