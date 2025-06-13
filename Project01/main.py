from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()



conn = MongoClient("")



