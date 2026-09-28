def test_to_json_period_index(self):
    idx = pd.period_range('2016', freq='Q-JAN', periods=2)
    data = pd.Series(1, idx)
    result = data.to_json(orient='table', date_format='iso')
    result = json.loads(result, object_pairs_hook=OrderedDict)
    result['schema'].pop('pandas_version')
    fields = [{'freq': 'Q-JAN', 'name': 'index', 'type': 'datetime'}, {'name': 'values', 'type': 'integer'}]
    schema = {'fields': fields, 'primaryKey': ['index']}
    data = [OrderedDict([('index', '2015-11-01T00:00:00.000Z'), ('values', 1)]), OrderedDict([('index', '2016-02-01T00:00:00.000Z'), ('values', 1)])]
    expected = OrderedDict([('schema', schema), ('data', data)])
    assert result == expected