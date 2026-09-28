@pytest.mark.parametrize('date_format', ['epoch', 'iso'])
@pytest.mark.parametrize('as_object', [True, False])
@pytest.mark.parametrize('date_typ', [datetime.date, datetime.datetime, pd.Timestamp])
def test_date_index_and_values(self, date_format, as_object, date_typ):
    data = [date_typ(year=2020, month=1, day=1), pd.NaT]
    if as_object:
        data.append('a')
    ser = pd.Series(data, index=data)
    result = ser.to_json(date_format=date_format)
    if date_format == 'epoch':
        expected = '{"1577836800000":1577836800000,"null":null}'
    else:
        expected = '{"2020-01-01T00:00:00.000Z":"2020-01-01T00:00:00.000Z","null":null}'
    if as_object:
        expected = expected.replace('}', ',"a":"a"}')
    assert result == expected