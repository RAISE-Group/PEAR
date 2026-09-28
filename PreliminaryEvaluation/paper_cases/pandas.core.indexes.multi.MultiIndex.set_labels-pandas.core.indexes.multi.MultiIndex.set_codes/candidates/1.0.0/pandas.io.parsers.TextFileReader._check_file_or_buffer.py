def _check_file_or_buffer(self, f, engine):
    if is_file_like(f):
        next_attr = '__next__'
        if engine != 'c' and (not hasattr(f, next_attr)):
            msg = "The 'python' engine cannot iterate through this file buffer."
            raise ValueError(msg)
    return engine