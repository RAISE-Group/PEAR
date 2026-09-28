def _get_column_name_list(self) -> List[str]:
    names: List[str] = []
    columns = self.frame.columns
    if isinstance(columns, ABCMultiIndex):
        names.extend(('' if name is None else name for name in columns.names))
    else:
        names.append('' if columns.name is None else columns.name)
    return names