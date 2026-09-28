def _conv(self, data):
    """
        Convert each input to appropriate for table outplot.
        """
    if isinstance(data, pd.Series):
        if data.name is None:
            data = data.to_frame(name='')
        else:
            data = data.to_frame()
    data = data.fillna('NaN')
    return data