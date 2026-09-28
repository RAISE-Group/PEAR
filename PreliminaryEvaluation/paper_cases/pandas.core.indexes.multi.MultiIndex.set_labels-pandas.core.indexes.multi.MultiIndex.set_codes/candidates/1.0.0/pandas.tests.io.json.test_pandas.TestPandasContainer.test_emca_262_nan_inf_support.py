def test_emca_262_nan_inf_support(self):
    data = '["a", NaN, "NaN", Infinity, "Infinity", -Infinity, "-Infinity"]'
    result = pd.read_json(data)
    expected = pd.DataFrame(['a', np.nan, 'NaN', np.inf, 'Infinity', -np.inf, '-Infinity'])
    tm.assert_frame_equal(result, expected)