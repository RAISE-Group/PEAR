@pytest.mark.parametrize('replacer', [pd.Timestamp('20170827'), np.int8(1), np.int16(1), np.float32(1), np.float64(1)])
def test_replace_replacer_dtype(self, replacer):
    df = pd.DataFrame(['a'])
    result = df.replace({'a': replacer, 'b': replacer})
    expected = pd.DataFrame([replacer])
    tm.assert_frame_equal(result, expected)