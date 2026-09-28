@pytest.mark.parametrize('date_dtype', [np.datetime64, np.dtype('<M8[ns]'), PeriodDtype('D'), DatetimeTZDtype('ns', 'US/Central')])
def test_as_json_table_type_date_dtypes(self, date_dtype):
    assert as_json_table_type(date_dtype) == 'datetime'