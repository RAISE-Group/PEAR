def test_astype_mixed_float(self, mixed_float_frame):
    casted = mixed_float_frame.reindex(columns=['A', 'B']).astype('float32')
    _check_cast(casted, 'float32')
    casted = mixed_float_frame.reindex(columns=['A', 'B']).astype('float16')
    _check_cast(casted, 'float16')