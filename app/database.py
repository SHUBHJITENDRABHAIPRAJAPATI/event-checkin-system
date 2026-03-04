// app/database.py
// shubh prajapati

// Database setup for the event check-in system using SQLAlchemy
// This file defines the database connection, session management, and base class for models.



from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./events.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()