import re
from .repository import EventRepository, AttendeeRepository

class EventService:
     def __init__(self, db):
          self.db = db
          self.event_repo = EventRepository(db)
          self.attendee_repo = AttendeeRepository(db)

     def create_event(self, name, date):
          return self.event_repo.create(name, date)

     def register_attendee(self, event_id, name, email):
          if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
               raise ValueError("Invalid email")

          if self.attendee_repo.exists(event_id, email):
               raise ValueError("Duplicate registration")

          return self.attendee_repo.create(event_id, name, email)

     def check_in(self, event_id, email):
          attendee = self.attendee_repo.get_by_email(event_id, email)

          if not attendee:
               raise ValueError("Not registered")

          if attendee.checked_in:
               raise ValueError("Already checked in")

          attendee.checked_in = True
          self.db.commit()
          return attendee

     def generate_report(self, event_id):
          event = self.event_repo.get(event_id)
          attendees = self.attendee_repo.get_by_event(event_id)

          checked = [a for a in attendees if a.checked_in]

          return {
               "event_name": event.name,
               "total_registered": len(attendees),
               "total_checked_in": len(checked),
               "checked_in_attendees": [a.email for a in checked]
          }
