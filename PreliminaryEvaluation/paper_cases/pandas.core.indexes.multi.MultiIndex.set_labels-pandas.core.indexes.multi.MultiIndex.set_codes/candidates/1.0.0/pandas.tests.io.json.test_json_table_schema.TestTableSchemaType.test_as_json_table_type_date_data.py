@pytest.mark.parametrize('date_data', [pd.to_datetime(['2016']), pd.to_datetime(['2016'], utc=True), pd.Series(pd.to_datetime(['2016'])), pd.Series(pd.to_datetime(['2016'], utc=True)), pd.period_range('2016', freq='A', periods=3)])
def test_as_json_table_type_date_data(self, date_data):
    assert as_json_table_type(date_data) == 'datetime'