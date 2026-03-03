from app.database import SessionLocal, Base, engine
from app.services import EventService
from datetime import date

def setup_module():
     Base.metadata.create_all(bind=engine)

def test_full_workflow():
     db = SessionLocal()
     service = EventService(db)

     event = service.create_event("Conference", date.today())
     service.register_attendee(event.id, "John", "john@test.com")
     service.check_in(event.id, "john@test.com")

     report = service.generate_report(event.id)

     assert report["total_registered"] == 1
     assert report["total_checked_in"] == 1

def test_registration_persistence():
     db = SessionLocal()
     service = EventService(db)

     event = service.create_event("Workshop", date.today())
     service.register_attendee(event.id, "Alice", "alice@test.com")

     report = service.generate_report(event.id)

     assert report["total_registered"] == 1
     assert report["total_checked_in"] == 0

def test_multiple_attendees():
     db = SessionLocal()
     service = EventService(db)

     event = service.create_event("Seminar", date.today())
     service.register_attendee(event.id, "A", "a@test.com")
     service.register_attendee(event.id, "B", "b@test.com")

     report = service.generate_report(event.id)

     assert report["total_registered"] == 2