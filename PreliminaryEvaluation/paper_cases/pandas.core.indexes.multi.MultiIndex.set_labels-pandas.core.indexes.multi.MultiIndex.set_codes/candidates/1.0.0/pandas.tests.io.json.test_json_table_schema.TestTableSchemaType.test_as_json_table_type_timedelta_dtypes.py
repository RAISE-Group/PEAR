@pytest.mark.parametrize('td_dtype', [np.timedelta64, np.dtype('<m8[ns]')])
def test_as_json_table_type_timedelta_dtypes(self, td_dtype):
    assert as_json_table_type(td_dtype) == 'duration'