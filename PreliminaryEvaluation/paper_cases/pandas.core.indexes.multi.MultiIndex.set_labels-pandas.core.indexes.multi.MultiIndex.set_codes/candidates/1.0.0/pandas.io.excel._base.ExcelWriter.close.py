def close(self):
    """synonym for save, to make it more file-like"""
    return self.save()