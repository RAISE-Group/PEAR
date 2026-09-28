def test_complex_raises(self):
    df = DataFrame({'a': [1 + 1j, 2j]})
    msg = 'Complex datatypes not supported'
    with pytest.raises(ValueError, match=msg):
        df.to_sql('test_complex', self.conn)