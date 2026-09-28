@staticmethod
def _highlight_extrema(data, color='yellow', max_=True):
    """
        Highlight the min or max in a Series or DataFrame.
        """
    attr = f'background-color: {color}'
    if max_:
        extrema = data == np.nanmax(data.to_numpy())
    else:
        extrema = data == np.nanmin(data.to_numpy())
    if data.ndim == 1:
        return [attr if v else '' for v in extrema]
    else:
        return pd.DataFrame(np.where(extrema, attr, ''), index=data.index, columns=data.columns)