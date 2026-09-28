def execute(self, *args, **kwargs):
    """Simple passthrough to SQLAlchemy connectable"""
    return self.connectable.execute(*args, **kwargs)