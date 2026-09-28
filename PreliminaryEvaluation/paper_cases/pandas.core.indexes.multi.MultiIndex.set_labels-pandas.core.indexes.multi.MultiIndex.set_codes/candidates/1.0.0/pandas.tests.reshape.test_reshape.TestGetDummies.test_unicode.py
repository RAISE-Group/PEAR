def test_unicode(self, sparse):
    import unicodedata
    e = 'e'
    eacute = unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE')
    s = [e, eacute, eacute]
    res = get_dummies(s, prefix='letter', sparse=sparse)
    exp = DataFrame({'letter_e': [1, 0, 0], 'letter_{eacute}'.format(eacute=eacute): [0, 1, 1]}, dtype=np.uint8)
    if sparse:
        exp = exp.apply(SparseArray, fill_value=0)
    tm.assert_frame_equal(res, exp)