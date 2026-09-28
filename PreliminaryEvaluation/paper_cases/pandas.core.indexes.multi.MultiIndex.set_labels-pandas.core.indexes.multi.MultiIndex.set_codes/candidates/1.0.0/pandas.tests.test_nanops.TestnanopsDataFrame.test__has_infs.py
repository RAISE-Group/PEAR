def test__has_infs(self):
    pairs = [('arr_complex', False), ('arr_int', False), ('arr_bool', False), ('arr_str', False), ('arr_utf', False), ('arr_complex', False), ('arr_complex_nan', False), ('arr_nan_nanj', False), ('arr_nan_infj', True), ('arr_complex_nan_infj', True)]
    pairs_float = [('arr_float', False), ('arr_nan', False), ('arr_float_nan', False), ('arr_nan_nan', False), ('arr_float_inf', True), ('arr_inf', True), ('arr_nan_inf', True), ('arr_float_nan_inf', True), ('arr_nan_nan_inf', True)]
    for arr, correct in pairs:
        val = getattr(self, arr)
        self.check_bool(nanops._has_infs, val, correct)
    for arr, correct in pairs_float:
        val = getattr(self, arr)
        self.check_bool(nanops._has_infs, val, correct)
        self.check_bool(nanops._has_infs, val.astype('f4'), correct)
        self.check_bool(nanops._has_infs, val.astype('f2'), correct)