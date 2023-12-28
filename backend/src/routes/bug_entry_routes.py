from flask import Blueprint
from controllers.bug_entry_controller import create_bug_entry

bug_entry_bp = Blueprint('bug_entry', __name__, url_prefix='/bug_entries')


@bug_entry_bp.route('/', method=['POST'])
def create_bug_entry_route():
    return create_bug_entry()
