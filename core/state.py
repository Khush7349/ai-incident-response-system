from collections import defaultdict
class StateManager:
    def __init__(self):
        self._state = defaultdict(dict)
    def get(self):
        return self._state
    def get_user(self, user: str):
        return self._state[user]
    def update(self, user: str, key: str, value):
        self._state[user][key] = value
    def reset(self):
        self._state.clear()