import pytest
from unittest.mock import MagicMock
from app.services import EventService

def setup_service():
     db = MagicMock()
     service = EventService(db)
     service.attendee_repo = MagicMock()
     service.event_repo = MagicMock()
     return service

def test_invalid_email():
     service = setup_service()
     with pytest.raises(ValueError):
          service.register_attendee(1, "John", "bademail")

def test_duplicate_registration():
     service = setup_service()
     service.attendee_repo.exists.return_value = True
     with pytest.raises(ValueError):
          service.register_attendee(1, "John", "john@test.com")

def test_checkin_not_registered():
     service = setup_service()
     service.attendee_repo.get_by_email.return_value = None
     with pytest.raises(ValueError):
          service.check_in(1, "john@test.com")

def test_checkin_already_done():
     service = setup_service()
     mock = MagicMock()
     mock.checked_in = True
     service.attendee_repo.get_by_email.return_value = mock
     with pytest.raises(ValueError):
          service.check_in(1, "john@test.com")

def test_report_counts():
     service = setup_service()
     event = MagicMock()
     event.name = "Test"
     service.event_repo.get.return_value = event

     a1 = MagicMock(email="a@test.com", checked_in=True)
     a2 = MagicMock(email="b@test.com", checked_in=False)
     service.attendee_repo.get_by_event.return_value = [a1, a2]

     report = service.generate_report(1)
     assert report["total_registered"] == 2
     assert report["total_checked_in"] == 1