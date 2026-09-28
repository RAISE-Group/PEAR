def _parse_errorbars(self, label, err):
    """
        Look for error keyword arguments and return the actual errorbar data
        or return the error DataFrame/dict

        Error bars can be specified in several ways:
            Series: the user provides a pandas.Series object of the same
                    length as the data
            ndarray: provides a np.ndarray of the same length as the data
            DataFrame/dict: error values are paired with keys matching the
                    key in the plotted DataFrame
            str: the name of the column within the plotted DataFrame
        """
    if err is None:
        return None

    def match_labels(data, e):
        e = e.reindex(data.index)
        return e
    if isinstance(err, ABCDataFrame):
        err = match_labels(self.data, err)
    elif isinstance(err, dict):
        pass
    elif isinstance(err, ABCSeries):
        err = match_labels(self.data, err)
        err = np.atleast_2d(err)
        err = np.tile(err, (self.nseries, 1))
    elif isinstance(err, str):
        evalues = self.data[err].values
        self.data = self.data[self.data.columns.drop(err)]
        err = np.atleast_2d(evalues)
        err = np.tile(err, (self.nseries, 1))
    elif is_list_like(err):
        if is_iterator(err):
            err = np.atleast_2d(list(err))
        else:
            err = np.atleast_2d(err)
        err_shape = err.shape
        if err.ndim == 3:
            if err_shape[0] != self.nseries or err_shape[1] != 2 or err_shape[2] != len(self.data):
                raise ValueError(f'Asymmetrical error bars should be provided with the shape ({self.nseries}, 2, {len(self.data)})')
        if len(err) == 1:
            err = np.tile(err, (self.nseries, 1))
    elif is_number(err):
        err = np.tile([err], (self.nseries, len(self.data)))
    else:
        msg = f'No valid {label} detected'
        raise ValueError(msg)
    return err