def _border_style(self, style: Optional[str], width):
    if width is None and style is None:
        return None
    if style == 'none' or style == 'hidden':
        return None
    if width is None:
        width = '2pt'
    width = float(width[:-2])
    if width < 1e-05:
        return None
    elif width < 1.3:
        width_name = 'thin'
    elif width < 2.8:
        width_name = 'medium'
    else:
        width_name = 'thick'
    if style in (None, 'groove', 'ridge', 'inset', 'outset'):
        style = 'solid'
    if style == 'double':
        return 'double'
    if style == 'solid':
        return width_name
    if style == 'dotted':
        if width_name in ('hair', 'thin'):
            return 'dotted'
        return 'mediumDashDotDot'
    if style == 'dashed':
        if width_name in ('hair', 'thin'):
            return 'dashed'
        return 'mediumDashed'