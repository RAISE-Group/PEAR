@pytest.mark.parametrize('infer_word', ['trade_time', 'date', 'datetime', 'sold_at', 'modified', 'timestamp', 'timestamps'])
def test_convert_dates_infer(self, infer_word):
    from pandas.io.json import dumps
    data = [{'id': 1, infer_word: 1036713600000}, {'id': 2}]
    expected = DataFrame([[1, Timestamp('2002-11-08')], [2, pd.NaT]], columns=['id', infer_word])
    result = read_json(dumps(data))[['id', infer_word]]
    tm.assert_frame_equal(result, expected)