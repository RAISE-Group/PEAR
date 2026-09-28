def copy(self, deep=True):
    """
        Make deep or shallow copy of BlockManager

        Parameters
        ----------
        deep : bool or string, default True
            If False, return shallow copy (do not copy data)
            If 'all', copy data and a deep copy of the index

        Returns
        -------
        BlockManager
        """
    if deep:

        def copy_func(ax):
            if deep == 'all':
                return ax.copy(deep=True)
            else:
                return ax.view()
        new_axes = [copy_func(ax) for ax in self.axes]
    else:
        new_axes = list(self.axes)
    res = self.apply('copy', deep=deep)
    res.axes = new_axes
    return res