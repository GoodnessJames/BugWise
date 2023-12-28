from flask import request, jsonify
from models.bug_entry_model import BugEntry
from utils.audio_utils import record_audio, save_audio
from config.database_config import db_session
from datetime import datetime


def create_bug_entry():
    try:
        # Parse request data
        title = request.json.get('title')
        user_id = request.json.get('user_id')

        # Record and save audio
        audio_file_path = f'audio/{user_id}_{datetime.now().strftime("%Y%m%d%H%M%S")}.wav'
        record_audio(audio_file_path)

        # Create bug entry in the database
        bug_entry = BugEntry(title=title, audio_recording_url=audio_file_path)

        # Add the bug entry to the session and commit to the database
        db_session.add(bug_entry)
        db_session.commit()

        return jsonify({"message": "Bug entry created successfully!"}), 201

    except Exception as e:
        db_session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db_session.close()
