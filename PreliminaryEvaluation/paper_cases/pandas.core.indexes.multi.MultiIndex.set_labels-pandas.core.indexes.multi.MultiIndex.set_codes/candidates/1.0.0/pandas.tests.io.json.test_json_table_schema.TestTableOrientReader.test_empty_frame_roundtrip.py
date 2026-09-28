def test_empty_frame_roundtrip(self):
    df = pd.DataFrame(columns=['a', 'b', 'c'])
    expected = df.copy()
    out = df.to_json(orient='table')
    result = pd.read_json(out, orient='table')
    tm.assert_frame_equal(expected, result)