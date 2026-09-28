@pytest.mark.parametrize('index_names', [[None, None], ['foo', 'bar'], ['foo', None], [None, 'foo'], ['index', 'foo']])
def test_multiindex(self, index_names):
    df = pd.DataFrame([['Arr', 'alpha', [1, 2, 3, 4]], ['Bee', 'Beta', [10, 20, 30, 40]]], index=[['A', 'B'], ['Null', 'Eins']], columns=['Aussprache', 'Griechisch', 'Args'])
    df.index.names = index_names
    out = df.to_json(orient='table')
    result = pd.read_json(out, orient='table')
    tm.assert_frame_equal(df, result)