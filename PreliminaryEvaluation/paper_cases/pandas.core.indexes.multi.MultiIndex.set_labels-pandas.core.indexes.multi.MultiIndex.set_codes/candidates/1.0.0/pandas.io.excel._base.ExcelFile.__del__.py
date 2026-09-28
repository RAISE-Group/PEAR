def __del__(self):
    try:
        self.close()
    except AttributeError:
        pass