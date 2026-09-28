def _check_for_bom(self, first_row):
    """
        Checks whether the file begins with the BOM character.
        If it does, remove it. In addition, if there is quoting
        in the field subsequent to the BOM, remove it as well
        because it technically takes place at the beginning of
        the name, not the middle of it.
        """
    if not first_row:
        return first_row
    if not isinstance(first_row[0], str):
        return first_row
    if not first_row[0]:
        return first_row
    first_elt = first_row[0][0]
    if first_elt != _BOM:
        return first_row
    first_row_bom = first_row[0]
    if len(first_row_bom) > 1 and first_row_bom[1] == self.quotechar:
        start = 2
        quote = first_row_bom[1]
        end = first_row_bom[2:].index(quote) + 2
        new_row = first_row_bom[start:end]
        if len(first_row_bom) > end + 1:
            new_row += first_row_bom[end + 1:]
        return [new_row] + first_row[1:]
    elif len(first_row_bom) > 1:
        return [first_row_bom[1:]]
    else:
        return ['']