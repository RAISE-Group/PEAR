def write_td(self, s: Any, indent: int=0, tags: Optional[str]=None) -> None:
    self._write_cell(s, kind='td', indent=indent, tags=tags)