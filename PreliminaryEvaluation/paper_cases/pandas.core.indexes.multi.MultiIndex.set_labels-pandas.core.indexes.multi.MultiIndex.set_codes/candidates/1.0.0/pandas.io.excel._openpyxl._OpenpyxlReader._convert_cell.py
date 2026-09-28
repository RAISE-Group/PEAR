def _convert_cell(self, cell, convert_float: bool) -> Scalar:
    if cell.is_date:
        return cell.value
    elif cell.data_type == 'e':
        return np.nan
    elif cell.data_type == 'b':
        return bool(cell.value)
    elif cell.value is None:
        return ''
    elif cell.data_type == 'n':
        if convert_float:
            val = int(cell.value)
            if val == cell.value:
                return val
        else:
            return float(cell.value)
    return cell.value