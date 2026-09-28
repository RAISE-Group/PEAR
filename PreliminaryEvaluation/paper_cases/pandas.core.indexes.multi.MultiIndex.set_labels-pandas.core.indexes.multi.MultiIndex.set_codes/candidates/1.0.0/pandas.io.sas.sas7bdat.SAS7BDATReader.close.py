def close(self):
    try:
        self.handle.close()
    except AttributeError:
        pass