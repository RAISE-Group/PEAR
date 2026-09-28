def __repr__(self) -> str:
    data = self._format_data()
    class_name = f'<{type(self).__name__}>\n'
    template = f'{class_name}{data}\nLength: {len(self)}, closed: {self.closed}, dtype: {self.dtype}'
    return template