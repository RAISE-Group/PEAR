def test_extract_expand_None(self):
    values = Series(['fooBAD__barBAD', np.nan, 'foo'])
    with pytest.raises(ValueError, match='expand must be True or False'):
        values.str.extract('.*(BAD[_]+).*(BAD)', expand=None)