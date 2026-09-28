def test_extract_expand_unspecified(self):
    values = Series(['fooBAD__barBAD', np.nan, 'foo'])
    result_unspecified = values.str.extract('.*(BAD[_]+).*')
    assert isinstance(result_unspecified, DataFrame)
    result_true = values.str.extract('.*(BAD[_]+).*', expand=True)
    tm.assert_frame_equal(result_unspecified, result_true)