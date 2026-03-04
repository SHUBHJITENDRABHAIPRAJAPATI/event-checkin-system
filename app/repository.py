// app/repository.py
// shubh prajapati
// Repository layer for the event check-in system using SQLAlchemy



from .models import Event, Attendee

class EventRepository:
     def __init__(self, db):
          self.db = db

     def create(self, name, date):
          event = Event(name=name, date=date)
          self.db.add(event)
          self.db.commit()
          self.db.refresh(event)
          return event

     def get(self, event_id):
          return self.db.query(Event).filter(Event.id == event_id).first()


class AttendeeRepository:
     def __init__(self, db):
          self.db = db

     def create(self, event_id, name, email):
          attendee = Attendee(name=name, email=email, event_id=event_id)
          self.db.add(attendee)
          self.db.commit()
          self.db.refresh(attendee)
          return attendee

     def exists(self, event_id, email):
          return self.db.query(Attendee).filter(
               Attendee.event_id == event_id,
               Attendee.email == email
          ).first() is not None

     def get_by_email(self, event_id, email):
          return self.db.query(Attendee).filter(
          Attendee.event_id == event_id,
          Attendee.email == email
          ).first()

     def get_by_event(self, event_id):
          return self.db.query(Attendee).filter(
               Attendee.event_id == event_id
          ).all()
          