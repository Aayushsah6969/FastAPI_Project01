from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
templates=Jinja2Templates(directory="templates")

note = APIRouter()

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # Fetching data from MongoDB
    docs = conn.AllNotes.Notes.find({})
    newDocs = []
    # Transforming the data to a simpler format
    for doc in docs:
        newDocs.append({
            "id":doc["_id"],
            "note":doc["note"],
        })
    return templates.TemplateResponse("index.html",{ "request":request, "newDocs":newDocs,})