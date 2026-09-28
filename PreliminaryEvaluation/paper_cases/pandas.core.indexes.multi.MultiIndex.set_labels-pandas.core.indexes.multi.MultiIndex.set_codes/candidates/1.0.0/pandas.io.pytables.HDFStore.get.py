def get(self, key: str):
    """
        Retrieve pandas object stored in file.

        Parameters
        ----------
        key : str

        Returns
        -------
        object
            Same type as object stored in file.
        """
    group = self.get_node(key)
    if group is None:
        raise KeyError(f'No object named {key} in the file')
    return self._read_group(group)