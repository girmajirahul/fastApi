
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse, HTMLResponse
from routes.note import note
from fastapi.staticfiles import StaticFiles


app=FastAPI()
app.include_router(note)

app.mount("/static", StaticFiles(directory="static"), name="static")