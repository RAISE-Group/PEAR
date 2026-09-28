def test_to_string(self):
    buf = StringIO()
    s = self.ts.to_string()
    retval = self.ts.to_string(buf=buf)
    assert retval is None
    assert buf.getvalue().strip() == s
    format = '%.4f'.__mod__
    result = self.ts.to_string(float_format=format)
    result = [x.split()[1] for x in result.split('\n')[:-1]]
    expected = [format(x) for x in self.ts]
    assert result == expected
    result = self.ts[:0].to_string()
    assert result == 'Series([], Freq: B)'
    result = self.ts[:0].to_string(length=0)
    assert result == 'Series([], Freq: B)'
    cp = self.ts.copy()
    cp.name = 'foo'
    result = cp.to_string(length=True, name=True, dtype=True)
    last_line = result.split('\n')[-1].strip()
    assert last_line == f'Freq: B, Name: foo, Length: {len(cp)}, dtype: float64'