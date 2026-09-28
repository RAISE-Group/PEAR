@pytest.mark.skipif(not PYPY, reason='on PyPy deep=True does not change result')
def test_info_memory_usage_deep_pypy(self):
    df_with_object_index = pd.DataFrame({'a': [1]}, index=['foo'])
    assert df_with_object_index.memory_usage(index=True, deep=True).sum() == df_with_object_index.memory_usage(index=True).sum()
    df_object = pd.DataFrame({'a': ['a']})
    assert df_object.memory_usage(deep=True).sum() == df_object.memory_usage().sum()