def _write(self, obj, orient, double_precision, ensure_ascii, date_unit, iso_dates, default_handler, indent):
    table_obj = {'schema': self.schema, 'data': obj}
    serialized = super()._write(table_obj, orient, double_precision, ensure_ascii, date_unit, iso_dates, default_handler, indent)
    return serialized