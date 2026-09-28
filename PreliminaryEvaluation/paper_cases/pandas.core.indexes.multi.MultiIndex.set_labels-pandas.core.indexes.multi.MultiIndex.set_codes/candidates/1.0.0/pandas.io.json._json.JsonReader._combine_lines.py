def _combine_lines(self, lines) -> str:
    """
        Combines a list of JSON objects into one JSON object.
        """
    lines = filter(None, map(lambda x: x.strip(), lines))
    return '[' + ','.join(lines) + ']'