class Memory:
    def __init__(self):
        self.store = {}

    def save(self, key: str, value: str):
        self.store[key] = value

    def get(self, key: str):
        return self.store.get(key, "")
