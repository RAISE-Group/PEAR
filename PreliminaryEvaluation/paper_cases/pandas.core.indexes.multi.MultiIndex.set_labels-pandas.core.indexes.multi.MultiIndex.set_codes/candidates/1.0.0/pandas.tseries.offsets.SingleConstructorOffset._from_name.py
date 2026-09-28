@classmethod
def _from_name(cls, suffix=None):
    if suffix:
        raise ValueError(f'Bad freq suffix {suffix}')
    return cls()