def close(self):
    for f in self.handles:
        f.close()