import threading
from datetime import datetime

class URLStore:
    def __init__(self):
        self.lock = threading.Lock()
        self.data = {}

    def save_url(self, short_code, original_url):
        with self.lock:
            self.data[short_code] = {
                "url": original_url,
                "created_at": datetime.utcnow().isoformat(),
                "clicks": 0
            }

    def get_url(self, short_code):
        with self.lock:
            return self.data.get(short_code)

    def increment_click(self, short_code):
        with self.lock:
            if short_code in self.data:
                self.data[short_code]["clicks"] += 1
