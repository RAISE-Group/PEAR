@pytest.mark.parametrize('data, fill_value', [(np.array([1, 2]), 0), (np.array([1.0, 2.0]), np.nan), ([True, False], False), ([pd.Timestamp('2017-01-01')], pd.NaT)])
def test_constructor_inferred_fill_value(self, data, fill_value):
    result = SparseArray(data).fill_value
    if pd.isna(fill_value):
        assert pd.isna(result)
    else:
        assert result == fill_value