@staticmethod
def _bar(s, align, colors, width=100, vmin=None, vmax=None):
    """
        Draw bar chart in dataframe cells.
        """
    smin = np.nanmin(s.to_numpy()) if vmin is None else vmin
    smax = np.nanmax(s.to_numpy()) if vmax is None else vmax
    if align == 'mid':
        smin = min(0, smin)
        smax = max(0, smax)
    elif align == 'zero':
        smax = max(abs(smin), abs(smax))
        smin = -smax
    normed = width * (s.to_numpy(dtype=float) - smin) / (smax - smin + 1e-12)
    zero = -width * smin / (smax - smin + 1e-12)

    def css_bar(start, end, color):
        """
            Generate CSS code to draw a bar from start to end.
            """
        css = 'width: 10em; height: 80%;'
        if end > start:
            css += 'background: linear-gradient(90deg,'
            if start > 0:
                css += f' transparent {start:.1f}%, {color} {start:.1f}%, '
            e = min(end, width)
            css += f'{color} {e:.1f}%, transparent {e:.1f}%)'
        return css

    def css(x):
        if pd.isna(x):
            return ''
        color = colors[1] if x > zero else colors[0]
        if align == 'left':
            return css_bar(0, x, color)
        else:
            return css_bar(min(x, zero), max(x, zero), color)
    if s.ndim == 1:
        return [css(x) for x in normed]
    else:
        return pd.DataFrame([[css(x) for x in row] for row in normed], index=s.index, columns=s.columns)