@classmethod
def _convert_to_font(cls, font_dict):
    """
        Convert ``font_dict`` to an openpyxl v2 Font object.

        Parameters
        ----------
        font_dict : dict
            A dict with zero or more of the following keys (or their synonyms).
                'name'
                'size' ('sz')
                'bold' ('b')
                'italic' ('i')
                'underline' ('u')
                'strikethrough' ('strike')
                'color'
                'vertAlign' ('vertalign')
                'charset'
                'scheme'
                'family'
                'outline'
                'shadow'
                'condense'

        Returns
        -------
        font : openpyxl.styles.Font
        """
    from openpyxl.styles import Font
    _font_key_map = {'sz': 'size', 'b': 'bold', 'i': 'italic', 'u': 'underline', 'strike': 'strikethrough', 'vertalign': 'vertAlign'}
    font_kwargs = {}
    for k, v in font_dict.items():
        if k in _font_key_map:
            k = _font_key_map[k]
        if k == 'color':
            v = cls._convert_to_color(v)
        font_kwargs[k] = v
    return Font(**font_kwargs)