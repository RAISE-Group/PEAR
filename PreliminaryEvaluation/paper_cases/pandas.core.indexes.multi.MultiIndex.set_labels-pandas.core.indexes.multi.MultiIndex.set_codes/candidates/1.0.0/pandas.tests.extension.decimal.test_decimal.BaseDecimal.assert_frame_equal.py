def assert_frame_equal(self, left, right, *args, **kwargs):
    tm.assert_index_equal(left.columns, right.columns, exact=kwargs.get('check_column_type', 'equiv'), check_names=kwargs.get('check_names', True), check_exact=kwargs.get('check_exact', False), check_categorical=kwargs.get('check_categorical', True), obj='{obj}.columns'.format(obj=kwargs.get('obj', 'DataFrame')))
    decimals = (left.dtypes == 'decimal').index
    for col in decimals:
        self.assert_series_equal(left[col], right[col], *args, **kwargs)
    left = left.drop(columns=decimals)
    right = right.drop(columns=decimals)
    tm.assert_frame_equal(left, right, *args, **kwargs)