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
    docs=conn.FAStApi.note.find({})
    newDocs=[]
    for doc in docs:
        newDocs.append({
            "id":doc["_id"],
            "title":doc["title"],
            "desc":doc["desc"],
            "important":doc["important"]
        })
    return templates.TemplateResponse("index.html",{"request":request,"newDocs":newDocs})


@note.post('/')
async def add_note(request:Request):
    form=await request.form()
    formDict=dict(form)
    formDict["important"]=True if formDict.get("important")=="on" else False
    inserted_note=conn.FAStApi.note.insert_one(formDict)
    return {"success":True}

from fastapi.responses import JSONResponse
from bson import ObjectId  # Make sure you import this

@note.get("/api/notes")
async def notes():
    docs = conn.FAStApi.note.find({})  
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),  
            "title": doc.get("title", ""),
            "desc": doc.get("desc", ""),
            "important": doc.get("important", False)
        })
    return JSONResponse(content=newDocs)

    

@note.get('/about',response_class=HTMLResponse)
async def read_items(request:Request):
    data=data = [
        {"name": "Rahul", "age": 23, "address": "Warje Pune"},
        {"name": "Mosin", "age": 22, "address": "Katraj Pune"},
       
    ]
    return templates.TemplateResponse("About.html",{"request":request,"data":data})