def test_info(self, float_frame, datetime_frame):
    io = StringIO()
    float_frame.info(buf=io)
    datetime_frame.info(buf=io)
    frame = DataFrame(np.random.randn(5, 3))
    frame.info()
    frame.info(verbose=False)