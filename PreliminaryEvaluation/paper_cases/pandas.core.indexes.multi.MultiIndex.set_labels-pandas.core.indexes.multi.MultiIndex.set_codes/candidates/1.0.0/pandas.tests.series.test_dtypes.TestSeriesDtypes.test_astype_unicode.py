def test_astype_unicode(self):
    digits = string.digits
    test_series = [Series([digits * 10, tm.rands(63), tm.rands(64), tm.rands(1000)]), Series(['データーサイエンス、お前はもう死んでいる'])]
    former_encoding = None
    if sys.getdefaultencoding() == 'utf-8':
        test_series.append(Series(['野菜食べないとやばい'.encode('utf-8')]))
    for s in test_series:
        res = s.astype('unicode')
        expec = s.map(str)
        tm.assert_series_equal(res, expec)
    if former_encoding is not None and former_encoding != 'utf-8':
        reload(sys)
        sys.setdefaultencoding(former_encoding)