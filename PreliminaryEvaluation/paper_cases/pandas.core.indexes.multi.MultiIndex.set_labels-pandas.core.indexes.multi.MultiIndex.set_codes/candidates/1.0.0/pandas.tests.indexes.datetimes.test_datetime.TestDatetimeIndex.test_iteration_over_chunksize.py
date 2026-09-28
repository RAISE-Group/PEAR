@pytest.mark.parametrize('periods', [0, 9999, 10000, 10001])
def test_iteration_over_chunksize(self, periods):
    index = date_range('2000-01-01 00:00:00', periods=periods, freq='min')
    num = 0
    for stamp in index:
        assert index[num] == stamp
        num += 1
    assert num == len(index)