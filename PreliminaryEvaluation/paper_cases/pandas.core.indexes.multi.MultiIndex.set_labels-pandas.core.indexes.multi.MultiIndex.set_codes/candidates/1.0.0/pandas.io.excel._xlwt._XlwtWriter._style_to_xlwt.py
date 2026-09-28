@classmethod
def _style_to_xlwt(cls, item, firstlevel: bool=True, field_sep=',', line_sep=';') -> str:
    """helper which recursively generate an xlwt easy style string
        for example:

            hstyle = {"font": {"bold": True},
            "border": {"top": "thin",
                    "right": "thin",
                    "bottom": "thin",
                    "left": "thin"},
            "align": {"horiz": "center"}}
            will be converted to
            font: bold on;                     border: top thin, right thin, bottom thin, left thin;                     align: horiz center;
        """
    if hasattr(item, 'items'):
        if firstlevel:
            it = [f'{key}: {cls._style_to_xlwt(value, False)}' for key, value in item.items()]
            out = f'{line_sep.join(it)} '
            return out
        else:
            it = [f'{key} {cls._style_to_xlwt(value, False)}' for key, value in item.items()]
            out = f'{field_sep.join(it)} '
            return out
    else:
        item = f'{item}'
        item = item.replace('True', 'on')
        item = item.replace('False', 'off')
        return item