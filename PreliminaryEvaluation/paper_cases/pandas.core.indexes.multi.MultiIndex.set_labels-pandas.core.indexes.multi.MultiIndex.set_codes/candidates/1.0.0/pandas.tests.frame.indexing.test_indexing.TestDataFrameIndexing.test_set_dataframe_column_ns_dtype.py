def test_set_dataframe_column_ns_dtype(self):
    x = DataFrame([datetime.now(), datetime.now()])
    assert x[0].dtype == np.dtype('M8[ns]')