def _get_stacking_id(self):
    if self.stacked:
        return id(self.data)
    else:
        return None