def test_do_not_mangle_na_values(self, unique_nulls_fixture, unique_nulls_fixture2):
    if unique_nulls_fixture is unique_nulls_fixture2:
        return
    a = np.array([unique_nulls_fixture, unique_nulls_fixture2], dtype=np.object)
    result = pd.unique(a)
    assert result.size == 2
    assert a[0] is unique_nulls_fixture
    assert a[1] is unique_nulls_fixture2