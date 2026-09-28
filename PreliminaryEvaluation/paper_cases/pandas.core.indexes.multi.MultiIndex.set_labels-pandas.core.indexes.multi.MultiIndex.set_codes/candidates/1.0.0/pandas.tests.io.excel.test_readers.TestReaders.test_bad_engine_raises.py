def test_bad_engine_raises(self, read_ext):
    bad_engine = 'foo'
    with pytest.raises(ValueError, match='Unknown engine: foo'):
        pd.read_excel('', engine=bad_engine)