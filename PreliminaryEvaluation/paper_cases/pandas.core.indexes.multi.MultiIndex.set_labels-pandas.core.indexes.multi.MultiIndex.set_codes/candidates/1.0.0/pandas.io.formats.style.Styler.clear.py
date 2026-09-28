def clear(self):
    """
        Reset the styler, removing any previously applied styles.

        Returns None.
        """
    self.ctx.clear()
    self._todo = []