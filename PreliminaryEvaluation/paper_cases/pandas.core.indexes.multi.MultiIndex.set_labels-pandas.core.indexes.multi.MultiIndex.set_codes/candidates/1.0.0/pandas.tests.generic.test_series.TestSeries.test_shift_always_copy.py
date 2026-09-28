@pytest.mark.parametrize('s', [Series([np.arange(5)]), pd.date_range('1/1/2011', periods=24, freq='H'), pd.Series(range(5), index=pd.date_range('2017', periods=5))])
@pytest.mark.parametrize('shift_size', [0, 1, 2])
def test_shift_always_copy(self, s, shift_size):
    assert s.shift(shift_size) is not s