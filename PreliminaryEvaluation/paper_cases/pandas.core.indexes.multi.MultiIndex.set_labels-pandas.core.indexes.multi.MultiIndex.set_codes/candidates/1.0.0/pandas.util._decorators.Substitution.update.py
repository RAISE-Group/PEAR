def update(self, *args, **kwargs) -> None:
    """
        Update self.params with supplied args.
        """
    if isinstance(self.params, dict):
        self.params.update(*args, **kwargs)