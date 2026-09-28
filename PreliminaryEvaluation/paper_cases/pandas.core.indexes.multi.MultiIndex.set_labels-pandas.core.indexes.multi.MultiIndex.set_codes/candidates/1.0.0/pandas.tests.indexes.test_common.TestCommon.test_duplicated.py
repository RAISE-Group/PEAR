@pytest.mark.parametrize('keep', ['first', 'last', False])
def test_duplicated(self, indices, keep):
    if not len(indices) or isinstance(indices, (MultiIndex, RangeIndex)):
        pytest.skip('Skip check for empty Index, MultiIndex, RangeIndex')
    holder = type(indices)
    idx = holder(indices)
    if idx.has_duplicates:
        idx = idx.drop_duplicates()
    n, k = (len(idx), 10)
    duplicated_selection = np.random.choice(n, k * n)
    expected = pd.Series(duplicated_selection).duplicated(keep=keep).values
    idx = holder(idx.values[duplicated_selection])
    result = idx.duplicated(keep=keep)
    tm.assert_numpy_array_equal(result, expected)