from fastapi import FastAPI
from datetime import date
from .database import engine, Base, SessionLocal
from .services import EventService

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/events/")
def create_event(name: str, event_date: date):
     db = SessionLocal()
     service = EventService(db)
     return service.create_event(name, event_date)

@app.post("/register/")
def register(event_id: int, name: str, email: str):
     db = SessionLocal()
     service = EventService(db)
     return service.register_attendee(event_id, name, email)

@app.post("/checkin/")
def checkin(event_id: int, email: str):
     db = SessionLocal()
     service = EventService(db)
     return service.check_in(event_id, email)

@app.get("/report/{event_id}")
def report(event_id: int):
     db = SessionLocal()
     service = EventService(db)
     return service.generate_report(event_id)