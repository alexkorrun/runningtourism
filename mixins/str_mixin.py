class StrMixin:
    def __str__(self) -> str:
        if hasattr(self, "title") and self.title:
            return self.title
        elif hasattr(self, "event_name") and self.event_name:
            return self.event_name