@pytest.mark.parametrize('method', ['pad', 'backfill'])
def test_fillna_method_doesnt_change_orig(self, method):
    data = np.arange(10, dtype='i8') * 24 * 3600 * 10 ** 9
    arr = self.array_cls(data, freq='D')
    arr[4] = pd.NaT
    fill_value = arr[3] if method == 'pad' else arr[5]
    result = arr.fillna(method=method)
    assert result[4] == fill_value
    assert arr[4] is pd.NaT