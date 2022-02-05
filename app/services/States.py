from models.models import State

from utils.db import db

class stateService():
    
        def __init__(self):
            pass
    
        def get_states(self):
            return State.query.all()
    
        def get_state_id(self, id_state):
            return State.query.filter_by(id_state=id_state).first()
    
        def create_state(self, state):
            new_state = State(state)
            db.session.add(new_state)
            db.session.commit()
            return "State created"
    
        def update_state(self, id_state, state):
            state_update = State.query.filter_by(id_state=id_state).first()
            state_update.state = state
            db.session.commit()
            return "State updated"
    
        def delete_state(self, id_state):
            state_delete = State.query.filter_by(id_state=id_state).first()
            db.session.delete(state_delete)
            db.session.commit()
            return "State deleted"