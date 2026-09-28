def update_info(self, info):
    """ set/update the info for this indexable with the key/value
            if there is a conflict raise/warn as needed """
    for key in self._info_fields:
        value = getattr(self, key, None)
        idx = info.setdefault(self.name, {})
        existing_value = idx.get(key)
        if key in idx and value is not None and (existing_value != value):
            if key in ['freq', 'index_name']:
                ws = attribute_conflict_doc % (key, existing_value, value)
                warnings.warn(ws, AttributeConflictWarning, stacklevel=6)
                idx[key] = None
                setattr(self, key, None)
            else:
                raise ValueError(f'invalid info for [{self.name}] for [{key}], existing_value [{existing_value}] conflicts with new value [{value}]')
        elif value is not None or existing_value is not None:
            idx[key] = value