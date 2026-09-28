def validate_names(self):
    if not Index(self.values).is_object():
        raise ValueError('cannot have non-object label DataIndexableCol')