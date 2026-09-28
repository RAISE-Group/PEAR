@pytest.mark.parametrize('index_nm', [None, 'idx', 'index'])
@pytest.mark.parametrize('vals', [{'timedeltas': pd.timedelta_range('1H', periods=4, freq='T')}, {'timezones': pd.date_range('2016-01-01', freq='d', periods=4, tz='US/Central')}])
def test_read_json_table_orient_raises(self, index_nm, vals, recwarn):
    df = DataFrame(vals, index=pd.Index(range(4), name=index_nm))
    out = df.to_json(orient='table')
    with pytest.raises(NotImplementedError, match='can not yet read '):
        pd.read_json(out, orient='table')