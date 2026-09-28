@classmethod
def _convert_to_color(cls, color_spec):
    """
        Convert ``color_spec`` to an openpyxl v2 Color object.

        Parameters
        ----------
        color_spec : str, dict
            A 32-bit ARGB hex string, or a dict with zero or more of the
            following keys.
                'rgb'
                'indexed'
                'auto'
                'theme'
                'tint'
                'index'
                'type'

        Returns
        -------
        color : openpyxl.styles.Color
        """
    from openpyxl.styles import Color
    if isinstance(color_spec, str):
        return Color(color_spec)
    else:
        return Color(**color_spec)