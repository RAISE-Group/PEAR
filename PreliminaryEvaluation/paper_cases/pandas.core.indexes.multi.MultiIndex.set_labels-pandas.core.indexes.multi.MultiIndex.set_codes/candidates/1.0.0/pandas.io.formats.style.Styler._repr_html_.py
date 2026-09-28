def _repr_html_(self):
    """
        Hooks into Jupyter notebook rich display system.
        """
    return self.render()