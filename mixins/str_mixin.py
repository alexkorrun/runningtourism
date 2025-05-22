class StrMixin:
    def __str__(self) -> str:
        if hasattr(self, "title") and self.title:
            return str(self.title)
        elif hasattr(self, "event_name") and self.event_name:
            return str(self.event_name)
        elif hasattr(self, "name") and self.name:
            return str(self.name)
        return f"{self.__class__.__name__} object ({self.pk})"