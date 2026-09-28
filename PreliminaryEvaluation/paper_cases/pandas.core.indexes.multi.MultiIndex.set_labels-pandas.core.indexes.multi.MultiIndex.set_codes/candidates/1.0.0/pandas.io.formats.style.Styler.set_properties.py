def set_properties(self, subset=None, **kwargs):
    """
        Method to set one or more non-data dependent properties or each cell.

        Parameters
        ----------
        subset : IndexSlice
            A valid slice for ``data`` to limit the style application to.
        **kwargs : dict
            A dictionary of property, value pairs to be set for each cell.

        Returns
        -------
        self : Styler

        Examples
        --------
        >>> df = pd.DataFrame(np.random.randn(10, 4))
        >>> df.style.set_properties(color="white", align="right")
        >>> df.style.set_properties(**{'background-color': 'yellow'})
        """
    values = ';'.join((f'{p}: {v}' for p, v in kwargs.items()))
    f = lambda x: values
    return self.applymap(f, subset=subset)