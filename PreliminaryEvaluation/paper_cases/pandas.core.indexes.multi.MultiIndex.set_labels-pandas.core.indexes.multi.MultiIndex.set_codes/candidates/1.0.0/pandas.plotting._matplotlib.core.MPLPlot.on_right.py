def on_right(self, i):
    if isinstance(self.secondary_y, bool):
        return self.secondary_y
    if isinstance(self.secondary_y, (tuple, list, np.ndarray, ABCIndexClass)):
        return self.data.columns[i] in self.secondary_y