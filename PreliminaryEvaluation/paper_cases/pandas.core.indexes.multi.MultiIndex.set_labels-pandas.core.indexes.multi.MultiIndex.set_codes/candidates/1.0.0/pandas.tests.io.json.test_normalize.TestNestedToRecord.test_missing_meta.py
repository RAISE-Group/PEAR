def test_missing_meta(self, missing_metadata):
    result = json_normalize(data=missing_metadata, record_path='addresses', meta='name', errors='ignore')
    ex_data = [[9562, 'Morris St.', 'Massillon', 'OH', 44646, 'Alice'], [8449, 'Spring St.', 'Elizabethton', 'TN', 37643, np.nan]]
    columns = ['city', 'number', 'state', 'street', 'zip', 'name']
    columns = ['number', 'street', 'city', 'state', 'zip', 'name']
    expected = DataFrame(ex_data, columns=columns)
    tm.assert_frame_equal(result, expected)