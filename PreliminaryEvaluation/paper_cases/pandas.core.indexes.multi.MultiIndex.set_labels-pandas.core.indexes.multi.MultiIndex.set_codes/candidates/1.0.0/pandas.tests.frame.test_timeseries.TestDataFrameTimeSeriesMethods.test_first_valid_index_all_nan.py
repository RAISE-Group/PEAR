@pytest.mark.parametrize('klass', [Series, DataFrame])
def test_first_valid_index_all_nan(self, klass):
    obj = klass([np.nan])
    assert obj.first_valid_index() is None
    assert obj.iloc[:0].first_valid_index() is None