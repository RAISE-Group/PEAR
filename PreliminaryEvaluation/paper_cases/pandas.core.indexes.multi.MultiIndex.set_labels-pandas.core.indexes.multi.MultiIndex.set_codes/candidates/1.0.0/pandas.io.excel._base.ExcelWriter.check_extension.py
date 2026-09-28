@classmethod
def check_extension(cls, ext):
    """checks that path's extension against the Writer's supported
        extensions.  If it isn't supported, raises UnsupportedFiletypeError."""
    if ext.startswith('.'):
        ext = ext[1:]
    if not any((ext in extension for extension in cls.supported_extensions)):
        msg = 'Invalid extension for engine'
        f"'{pprint_thing(cls.engine)}': '{pprint_thing(ext)}'"
        raise ValueError(msg)
    else:
        return True