class Singleton:
    import threading

    _lock = threading.Lock()
    _unique_instance = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        with cls._lock:
            if cls._unique_instance is None:
                cls._unique_instance = super().__new__(cls)
        return cls._unique_instance

    def __init__(self, value=None):
        if not hasattr(self, "value"):
            self.value = value

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        with type(self)._lock:
            self.value = value
        
