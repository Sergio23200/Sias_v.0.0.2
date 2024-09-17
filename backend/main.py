# main.py
from routers.admin import admin_router
from routers.affiliate import affiliate_router
from fastapi import FastAPI
from config.db import engine, Base
from middleware.error_handler import ErrorHandler
from models.Medical_appointments import Medical_appointments_model
from models.Admin import Admin_model
from models.Affilate import Affiliate_model
from models.Hospital import Hospital_model
from models.Ips import Ips_model
from models.Specialist import Specialist_model
from models.Medications import Medications_model
from routers.login import login_router

app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "0.0.1"
app.include_router(affiliate_router)
app.include_router(admin_router)
app.add_middleware(ErrorHandler)
app.include_router(login_router)
Base.metadata.create_all(bind=engine)
