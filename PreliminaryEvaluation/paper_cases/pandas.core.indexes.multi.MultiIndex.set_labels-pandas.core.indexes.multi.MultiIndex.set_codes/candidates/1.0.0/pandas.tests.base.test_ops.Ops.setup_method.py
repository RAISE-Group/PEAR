def setup_method(self, method):
    self.bool_index = tm.makeBoolIndex(10, name='a')
    self.int_index = tm.makeIntIndex(10, name='a')
    self.float_index = tm.makeFloatIndex(10, name='a')
    self.dt_index = tm.makeDateIndex(10, name='a')
    self.dt_tz_index = tm.makeDateIndex(10, name='a').tz_localize(tz='US/Eastern')
    self.period_index = tm.makePeriodIndex(10, name='a')
    self.string_index = tm.makeStringIndex(10, name='a')
    self.unicode_index = tm.makeUnicodeIndex(10, name='a')
    arr = np.random.randn(10)
    self.bool_series = Series(arr, index=self.bool_index, name='a')
    self.int_series = Series(arr, index=self.int_index, name='a')
    self.float_series = Series(arr, index=self.float_index, name='a')
    self.dt_series = Series(arr, index=self.dt_index, name='a')
    self.dt_tz_series = self.dt_tz_index.to_series()
    self.period_series = Series(arr, index=self.period_index, name='a')
    self.string_series = Series(arr, index=self.string_index, name='a')
    self.unicode_series = Series(arr, index=self.unicode_index, name='a')
    types = ['bool', 'int', 'float', 'dt', 'dt_tz', 'period', 'string', 'unicode']
    self.indexes = [getattr(self, f'{t}_index') for t in types]
    self.series = [getattr(self, f'{t}_series') for t in types]
    index = self.int_index
    self.float32_series = Series(arr.astype(np.float32), index=index, name='a')
    arr_int = np.random.choice(10, size=10, replace=False)
    self.int8_series = Series(arr_int.astype(np.int8), index=index, name='a')
    self.int16_series = Series(arr_int.astype(np.int16), index=index, name='a')
    self.int32_series = Series(arr_int.astype(np.int32), index=index, name='a')
    self.uint8_series = Series(arr_int.astype(np.uint8), index=index, name='a')
    self.uint16_series = Series(arr_int.astype(np.uint16), index=index, name='a')
    self.uint32_series = Series(arr_int.astype(np.uint32), index=index, name='a')
    nrw_types = ['float32', 'int8', 'int16', 'int32', 'uint8', 'uint16', 'uint32']
    self.narrow_series = [getattr(self, f'{t}_series') for t in nrw_types]
    self.objs = self.indexes + self.series + self.narrow_series