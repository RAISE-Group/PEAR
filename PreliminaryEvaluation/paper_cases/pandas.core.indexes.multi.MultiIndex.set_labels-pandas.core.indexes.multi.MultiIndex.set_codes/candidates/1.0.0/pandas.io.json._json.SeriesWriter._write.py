def _write(self, obj, orient: Optional[str], double_precision: int, ensure_ascii: bool, date_unit: str, iso_dates: bool, default_handler: Optional[Callable[[Any], JSONSerializable]], indent: int):
    if not self.index and orient == 'split':
        obj = {'name': obj.name, 'data': obj.values}
    return super()._write(obj, orient, double_precision, ensure_ascii, date_unit, iso_dates, default_handler, indent)