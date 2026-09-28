@pytest.mark.parametrize('dt_args,extra_exp', [({}, {}), ({'utc': True}, {'tz': 'UTC'})])
@pytest.mark.parametrize('wrapper', [None, pd.Series])
def test_convert_pandas_type_to_json_field_datetime(self, dt_args, extra_exp, wrapper):
    data = [1.0, 2.0, 3.0]
    data = pd.to_datetime(data, **dt_args)
    if wrapper is pd.Series:
        data = pd.Series(data, name='values')
    result = convert_pandas_type_to_json_field(data)
    expected = {'name': 'values', 'type': 'datetime'}
    expected.update(extra_exp)
    assert result == expected