from fastapi import APIRouter,Request
from fastapi.responses import JSONResponse, HTMLResponse
from models.note import Note
from config.db import conn
from schema.note import noteEntity , notesEntity
from fastapi.templating import Jinja2Templates

note=APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get('/',response_class=HTMLResponse)
async def read_items(request:Request):
    docs=conn.FAStApi.notes.find({})
    newDocs=[]
    for doc in docs:
        newDocs.append({
            "id":doc["_id"],
            "note":doc["note"]
        })
    return templates.TemplateResponse("index.html",{"request":request,"newDocs":newDocs})


@note.post('/')
def add_note(note:Note):
    inserted_note=conn.FAStApi.note.insert_one(dict(note))
    return noteEntity(inserted_note)

@note.get('/about',response_class=HTMLResponse)
async def read_items(request:Request):
    data=data = [
        {"name": "Rahul", "age": 23, "address": "Warje Pune"},
        {"name": "Mosin", "age": 22, "address": "Katraj Pune"},
       
    ]
    return templates.TemplateResponse("About.html",{"request":request,"data":data})