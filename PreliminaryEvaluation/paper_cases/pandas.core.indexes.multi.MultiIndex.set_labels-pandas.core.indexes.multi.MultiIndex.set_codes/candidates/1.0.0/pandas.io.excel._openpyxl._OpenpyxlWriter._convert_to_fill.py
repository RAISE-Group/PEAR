@classmethod
def _convert_to_fill(cls, fill_dict):
    """
        Convert ``fill_dict`` to an openpyxl v2 Fill object.

        Parameters
        ----------
        fill_dict : dict
            A dict with one or more of the following keys (or their synonyms),
                'fill_type' ('patternType', 'patterntype')
                'start_color' ('fgColor', 'fgcolor')
                'end_color' ('bgColor', 'bgcolor')
            or one or more of the following keys (or their synonyms).
                'type' ('fill_type')
                'degree'
                'left'
                'right'
                'top'
                'bottom'
                'stop'

        Returns
        -------
        fill : openpyxl.styles.Fill
        """
    from openpyxl.styles import PatternFill, GradientFill
    _pattern_fill_key_map = {'patternType': 'fill_type', 'patterntype': 'fill_type', 'fgColor': 'start_color', 'fgcolor': 'start_color', 'bgColor': 'end_color', 'bgcolor': 'end_color'}
    _gradient_fill_key_map = {'fill_type': 'type'}
    pfill_kwargs = {}
    gfill_kwargs = {}
    for k, v in fill_dict.items():
        pk = gk = None
        if k in _pattern_fill_key_map:
            pk = _pattern_fill_key_map[k]
        if k in _gradient_fill_key_map:
            gk = _gradient_fill_key_map[k]
        if pk in ['start_color', 'end_color']:
            v = cls._convert_to_color(v)
        if gk == 'stop':
            v = cls._convert_to_stop(v)
        if pk:
            pfill_kwargs[pk] = v
        elif gk:
            gfill_kwargs[gk] = v
        else:
            pfill_kwargs[k] = v
            gfill_kwargs[k] = v
    try:
        return PatternFill(**pfill_kwargs)
    except TypeError:
        return GradientFill(**gfill_kwargs)