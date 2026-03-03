from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Event(Base):
     __tablename__ = "events"

     id = Column(Integer, primary_key=True, index=True)
     name = Column(String, nullable=False)
     date = Column(Date, nullable=False)

     attendees = relationship("Attendee", back_populates="event")


class Attendee(Base):
     __tablename__ = "attendees"

     id = Column(Integer, primary_key=True, index=True)
     name = Column(String, nullable=False)
     email = Column(String, nullable=False)
     checked_in = Column(Boolean, default=False)

     event_id = Column(Integer, ForeignKey("events.id"))
     event = relationship("Event", back_populates="attendees")
