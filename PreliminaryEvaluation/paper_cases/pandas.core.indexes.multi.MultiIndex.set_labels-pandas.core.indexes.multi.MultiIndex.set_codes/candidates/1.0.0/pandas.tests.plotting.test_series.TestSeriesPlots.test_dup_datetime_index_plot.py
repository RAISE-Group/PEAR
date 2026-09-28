@pytest.mark.slow
def test_dup_datetime_index_plot(self):
    dr1 = date_range('1/1/2009', periods=4)
    dr2 = date_range('1/2/2009', periods=4)
    index = dr1.append(dr2)
    values = randn(index.size)
    s = Series(values, index=index)
    _check_plot_works(s.plot)