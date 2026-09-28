def _get_row_repeat(self, row) -> int:
    """Return number of times this row was repeated
        Repeating an empty row appeared to be a common way
        of representing sparse rows in the table.
        """
    from odf.namespaces import TABLENS
    return int(row.attributes.get((TABLENS, 'number-rows-repeated'), 1))