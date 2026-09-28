def test_frame_timeseries_to_records(self):
    index = date_range('1/1/2000', periods=10)
    df = DataFrame(np.random.randn(10, 3), index=index, columns=['a', 'b', 'c'])
    result = df.to_records()
    result['index'].dtype == 'M8[ns]'
    result = df.to_records(index=False)