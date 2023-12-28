from app import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime


class BugEntry:
    __tablename__ = 'bug_entries'
    id = db.Column(Integer, primary_key=True)
    title = db.Column(String, nullable=False)
    audio_recording_url = db.Column(String)
    timestamp = db.Column(DateTime, default=datetime.utcnow)
