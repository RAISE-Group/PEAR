def _is_empty_row(self, row) -> bool:
    """Helper function to find empty rows
        """
    for column in row.childNodes:
        if len(column.childNodes) > 0:
            return False
    return True