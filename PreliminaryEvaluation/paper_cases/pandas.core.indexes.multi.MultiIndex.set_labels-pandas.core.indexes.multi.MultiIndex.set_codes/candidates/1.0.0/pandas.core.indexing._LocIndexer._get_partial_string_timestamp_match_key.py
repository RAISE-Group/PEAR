def _get_partial_string_timestamp_match_key(self, key, labels):
    """
        Translate any partial string timestamp matches in key, returning the
        new key.

        (GH 10331)
        """
    if isinstance(labels, ABCMultiIndex):
        if isinstance(key, str) and labels.levels[0]._supports_partial_string_indexing:
            key = tuple([key] + [slice(None)] * (len(labels.levels) - 1))
        if isinstance(key, tuple):
            new_key = []
            for i, component in enumerate(key):
                if isinstance(component, str) and labels.levels[i]._supports_partial_string_indexing:
                    new_key.append(slice(component, component, None))
                else:
                    new_key.append(component)
            key = tuple(new_key)
    return key