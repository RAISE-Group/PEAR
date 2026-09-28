def _convert_cell(self, cell, convert_float: bool) -> Scalar:
    if cell.v is None:
        return ''
    if isinstance(cell.v, float) and convert_float:
        val = int(cell.v)
        if val == cell.v:
            return val
        else:
            return float(cell.v)
    return cell.v