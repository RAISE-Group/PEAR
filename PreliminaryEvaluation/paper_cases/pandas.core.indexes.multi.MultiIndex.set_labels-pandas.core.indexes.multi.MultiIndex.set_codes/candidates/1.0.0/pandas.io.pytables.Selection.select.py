def select(self):
    """
        generate the selection
        """
    if self.condition is not None:
        return self.table.table.read_where(self.condition.format(), start=self.start, stop=self.stop)
    elif self.coordinates is not None:
        return self.table.table.read_coordinates(self.coordinates)
    return self.table.table.read(start=self.start, stop=self.stop)