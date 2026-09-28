@staticmethod
def _tag(val, tag):
    """Surround val with <tag></tag>"""
    if isinstance(val, str):
        val = bytes(val, 'utf-8')
    return bytes('<' + tag + '>', 'utf-8') + val + bytes('</' + tag + '>', 'utf-8')