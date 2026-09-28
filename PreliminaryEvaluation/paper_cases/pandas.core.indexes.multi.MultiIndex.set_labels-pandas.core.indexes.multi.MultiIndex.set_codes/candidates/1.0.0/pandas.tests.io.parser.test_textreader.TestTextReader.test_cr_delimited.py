def test_cr_delimited(self):

    def _test(text, **kwargs):
        nice_text = text.replace('\r', '\r\n')
        result = TextReader(StringIO(text), **kwargs).read()
        expected = TextReader(StringIO(nice_text), **kwargs).read()
        assert_array_dicts_equal(result, expected)
    data = 'a,b,c\r1,2,3\r4,5,6\r7,8,9\r10,11,12'
    _test(data, delimiter=',')
    data = 'a  b  c\r1  2  3\r4  5  6\r7  8  9\r10  11  12'
    _test(data, delim_whitespace=True)
    data = 'a,b,c\r1,2,3\r4,5,6\r,88,9\r10,11,12'
    _test(data, delimiter=',')
    sample = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O\rAAAAA,BBBBB,0,0,0,0,0,0,0,0,0,0,0,0,0\r,BBBBB,0,0,0,0,0,0,0,0,0,0,0,0,0'
    _test(sample, delimiter=',')
    data = 'A  B  C\r  2  3\r4  5  6'
    _test(data, delim_whitespace=True)
    data = 'A B C\r2 3\r4 5 6'
    _test(data, delim_whitespace=True)