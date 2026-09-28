def hide_index(self):
    """
        Hide any indices from rendering.

        .. versionadded:: 0.23.0

        Returns
        -------
        self : Styler
        """
    self.hidden_index = True
    return self