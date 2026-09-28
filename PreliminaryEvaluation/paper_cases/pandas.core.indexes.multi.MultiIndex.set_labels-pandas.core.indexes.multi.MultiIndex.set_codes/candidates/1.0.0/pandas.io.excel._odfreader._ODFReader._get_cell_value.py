def _get_cell_value(self, cell, convert_float: bool) -> Scalar:
    from odf.namespaces import OFFICENS
    cell_type = cell.attributes.get((OFFICENS, 'value-type'))
    if cell_type == 'boolean':
        if str(cell) == 'TRUE':
            return True
        return False
    if cell_type is None:
        return self.empty_value
    elif cell_type == 'float':
        cell_value = float(cell.attributes.get((OFFICENS, 'value')))
        if cell_value == 0.0:
            return str(cell)
        if convert_float:
            val = int(cell_value)
            if val == cell_value:
                return val
        return cell_value
    elif cell_type == 'percentage':
        cell_value = cell.attributes.get((OFFICENS, 'value'))
        return float(cell_value)
    elif cell_type == 'string':
        return str(cell)
    elif cell_type == 'currency':
        cell_value = cell.attributes.get((OFFICENS, 'value'))
        return float(cell_value)
    elif cell_type == 'date':
        cell_value = cell.attributes.get((OFFICENS, 'date-value'))
        return pd.to_datetime(cell_value)
    elif cell_type == 'time':
        return pd.to_datetime(str(cell)).time()
    else:
        raise ValueError(f'Unrecognized type {cell_type}')