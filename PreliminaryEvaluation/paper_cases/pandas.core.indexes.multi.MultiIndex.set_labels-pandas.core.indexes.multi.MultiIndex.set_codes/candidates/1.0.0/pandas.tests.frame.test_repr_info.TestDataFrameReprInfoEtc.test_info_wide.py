def test_info_wide(self):
    from pandas import set_option, reset_option
    io = StringIO()
    df = DataFrame(np.random.randn(5, 101))
    df.info(buf=io)
    io = StringIO()
    df.info(buf=io, max_cols=101)
    rs = io.getvalue()
    assert len(rs.splitlines()) > 100
    xp = rs
    set_option('display.max_info_columns', 101)
    io = StringIO()
    df.info(buf=io)
    assert rs == xp
    reset_option('display.max_info_columns')