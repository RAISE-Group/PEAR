@classmethod
def _convert_to_style_kwargs(cls, style_dict):
    """
        Convert a style_dict to a set of kwargs suitable for initializing
        or updating-on-copy an openpyxl v2 style object.

        Parameters
        ----------
        style_dict : dict
            A dict with zero or more of the following keys (or their synonyms).
                'font'
                'fill'
                'border' ('borders')
                'alignment'
                'number_format'
                'protection'

        Returns
        -------
        style_kwargs : dict
            A dict with the same, normalized keys as ``style_dict`` but each
            value has been replaced with a native openpyxl style object of the
            appropriate class.
        """
    _style_key_map = {'borders': 'border'}
    style_kwargs = {}
    for k, v in style_dict.items():
        if k in _style_key_map:
            k = _style_key_map[k]
        _conv_to_x = getattr(cls, f'_convert_to_{k}', lambda x: None)
        new_v = _conv_to_x(v)
        if new_v:
            style_kwargs[k] = new_v
    return style_kwargs