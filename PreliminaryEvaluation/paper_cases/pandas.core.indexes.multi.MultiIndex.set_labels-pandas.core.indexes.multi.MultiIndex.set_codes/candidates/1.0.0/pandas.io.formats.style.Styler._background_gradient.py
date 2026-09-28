@staticmethod
def _background_gradient(s, cmap='PuBu', low=0, high=0, text_color_threshold=0.408, vmin: Optional[float]=None, vmax: Optional[float]=None):
    """
        Color background in a range according to the data.
        """
    if not isinstance(text_color_threshold, (float, int)) or not 0 <= text_color_threshold <= 1:
        msg = '`text_color_threshold` must be a value from 0 to 1.'
        raise ValueError(msg)
    with _mpl(Styler.background_gradient) as (plt, colors):
        smin = np.nanmin(s.to_numpy()) if vmin is None else vmin
        smax = np.nanmax(s.to_numpy()) if vmax is None else vmax
        rng = smax - smin
        norm = colors.Normalize(smin - rng * low, smax + rng * high)
        rgbas = plt.cm.get_cmap(cmap)(norm(s.to_numpy(dtype=float)))

        def relative_luminance(rgba):
            """
                Calculate relative luminance of a color.

                The calculation adheres to the W3C standards
                (https://www.w3.org/WAI/GL/wiki/Relative_luminance)

                Parameters
                ----------
                color : rgb or rgba tuple

                Returns
                -------
                float
                    The relative luminance as a value from 0 to 1
                """
            r, g, b = (x / 12.92 if x <= 0.03928 else (x + 0.055) / 1.055 ** 2.4 for x in rgba[:3])
            return 0.2126 * r + 0.7152 * g + 0.0722 * b

        def css(rgba):
            dark = relative_luminance(rgba) < text_color_threshold
            text_color = '#f1f1f1' if dark else '#000000'
            return f'background-color: {colors.rgb2hex(rgba)};color: {text_color};'
        if s.ndim == 1:
            return [css(rgba) for rgba in rgbas]
        else:
            return pd.DataFrame([[css(rgba) for rgba in row] for row in rgbas], index=s.index, columns=s.columns)