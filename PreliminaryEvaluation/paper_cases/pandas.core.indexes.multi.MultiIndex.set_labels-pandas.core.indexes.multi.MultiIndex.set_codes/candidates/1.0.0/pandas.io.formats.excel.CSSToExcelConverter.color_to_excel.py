def color_to_excel(self, val: Optional[str]):
    if val is None:
        return None
    if val.startswith('#') and len(val) == 7:
        return val[1:].upper()
    if val.startswith('#') and len(val) == 4:
        return (val[1] * 2 + val[2] * 2 + val[3] * 2).upper()
    try:
        return self.NAMED_COLORS[val]
    except KeyError:
        warnings.warn(f'Unhandled color format: {repr(val)}', CSSWarning)