def test_frame_index_to_string(self):
    index = PeriodIndex(['2011-1', '2011-2', '2011-3'], freq='M')
    frame = DataFrame(np.random.randn(3, 4), index=index)
    frame.to_string()