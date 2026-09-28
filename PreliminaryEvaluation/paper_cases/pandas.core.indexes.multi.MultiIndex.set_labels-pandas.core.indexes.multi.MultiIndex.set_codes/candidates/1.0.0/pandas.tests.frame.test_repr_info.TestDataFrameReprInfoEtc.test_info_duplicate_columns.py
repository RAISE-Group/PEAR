def test_info_duplicate_columns(self):
    io = StringIO()
    frame = DataFrame(np.random.randn(1500, 4), columns=['a', 'a', 'b', 'b'])
    frame.info(buf=io)