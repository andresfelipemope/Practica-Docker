from fastapi import FastAPI, Request, HTTPException
from pathlib import Path

app = FastAPI()

DEFAULT_DATA_DIR = Path("/data")
APP_DATA_DIR = Path(__file__).resolve().parent.parent / "data"
DATA_DIR = DEFAULT_DATA_DIR if DEFAULT_DATA_DIR.exists() else APP_DATA_DIR
DATA_DIR.mkdir(parents=True, exist_ok=True)
DATA_FILE = DATA_DIR / "notas.txt"


def read_notes() -> list[str]:
    if not DATA_FILE.exists():
        return []
    return [line.strip() for line in DATA_FILE.read_text(encoding="utf-8").splitlines() if line.strip()]


def append_note(text: str) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with DATA_FILE.open("a", encoding="utf-8") as f:
        f.write(text.rstrip() + "\n")


@app.get("/")
async def root():
    return {
        "message": "API de notas con FastAPI y Docker",
        "notes": read_notes(),
        "data_file": str(DATA_FILE)
    }


@app.post("/nota")
async def create_note(request: Request):
    body = await request.body()
    text = body.decode("utf-8").strip()
    if not text:
        raise HTTPException(status_code=400, detail="El cuerpo de la petición no puede estar vacío")
    append_note(text)
    return {"status": "ok", "note": text, "total_notes": len(read_notes())}
