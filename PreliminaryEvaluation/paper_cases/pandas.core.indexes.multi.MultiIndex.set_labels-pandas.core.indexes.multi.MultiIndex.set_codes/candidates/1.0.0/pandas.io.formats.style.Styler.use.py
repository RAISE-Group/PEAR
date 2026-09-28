def use(self, styles):
    """
        Set the styles on the current Styler.

        Possibly uses styles from ``Styler.export``.

        Parameters
        ----------
        styles : list
            List of style functions.

        Returns
        -------
        self : Styler

        See Also
        --------
        Styler.export
        """
    self._todo.extend(styles)
    return self