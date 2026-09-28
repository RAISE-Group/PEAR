@pytest.mark.parametrize('data,idx,expected_first,expected_last', [({'A': [1, 2, 3]}, [1, 1, 2], 1, 2), ({'A': [1, 2, 3]}, [1, 2, 2], 1, 2), ({'A': [1, 2, 3, 4]}, ['d', 'd', 'd', 'd'], 'd', 'd'), ({'A': [1, np.nan, 3]}, [1, 1, 2], 1, 2), ({'A': [np.nan, np.nan, 3]}, [1, 1, 2], 2, 2), ({'A': [1, np.nan, 3]}, [1, 2, 2], 1, 2)])
def test_first_last_valid(self, float_frame, data, idx, expected_first, expected_last):
    N = len(float_frame.index)
    mat = np.random.randn(N)
    mat[:5] = np.nan
    mat[-5:] = np.nan
    frame = DataFrame({'foo': mat}, index=float_frame.index)
    index = frame.first_valid_index()
    assert index == frame.index[5]
    index = frame.last_valid_index()
    assert index == frame.index[-6]
    empty = DataFrame()
    assert empty.last_valid_index() is None
    assert empty.first_valid_index() is None
    frame[:] = np.nan
    assert frame.last_valid_index() is None
    assert frame.first_valid_index() is None
    frame.index = date_range('20110101', periods=N, freq='B')
    frame.iloc[1] = 1
    frame.iloc[-2] = 1
    assert frame.first_valid_index() == frame.index[1]
    assert frame.last_valid_index() == frame.index[-2]
    assert frame.first_valid_index().freq == frame.index.freq
    assert frame.last_valid_index().freq == frame.index.freq
    df = DataFrame(data, index=idx)
    assert expected_first == df.first_valid_index()
    assert expected_last == df.last_valid_index()