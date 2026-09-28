def close(self):
    if self.auto_close:
        self.store.close()