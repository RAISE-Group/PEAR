def _get_column_repeat(self, cell) -> int:
    from odf.namespaces import TABLENS
    return int(cell.attributes.get((TABLENS, 'number-columns-repeated'), 1))