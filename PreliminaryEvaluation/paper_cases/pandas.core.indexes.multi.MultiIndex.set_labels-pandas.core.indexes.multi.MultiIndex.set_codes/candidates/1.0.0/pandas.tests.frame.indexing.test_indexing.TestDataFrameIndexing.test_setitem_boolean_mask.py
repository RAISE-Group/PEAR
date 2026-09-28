@pytest.mark.parametrize('mask_type', [lambda df: df > np.abs(df) / 2, lambda df: (df > np.abs(df) / 2).values], ids=['dataframe', 'array'])
def test_setitem_boolean_mask(self, mask_type, float_frame):
    df = float_frame.copy()
    mask = mask_type(df)
    result = df.copy()
    result[mask] = np.nan
    expected = df.copy()
    expected.values[np.array(mask)] = np.nan
    tm.assert_frame_equal(result, expected)