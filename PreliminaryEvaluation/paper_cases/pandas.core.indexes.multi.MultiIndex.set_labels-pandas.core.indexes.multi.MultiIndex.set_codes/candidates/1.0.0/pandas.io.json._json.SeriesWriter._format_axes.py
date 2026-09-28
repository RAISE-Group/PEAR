def _format_axes(self):
    if not self.obj.index.is_unique and self.orient == 'index':
        raise ValueError(f"Series index must be unique for orient='{self.orient}'")