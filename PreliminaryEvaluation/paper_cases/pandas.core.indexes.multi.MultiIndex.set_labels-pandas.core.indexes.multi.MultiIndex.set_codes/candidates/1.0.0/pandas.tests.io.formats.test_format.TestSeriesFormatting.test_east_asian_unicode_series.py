def test_east_asian_unicode_series(self):
    s = Series(['a', 'bb', 'CCC', 'D'], index=['あ', 'いい', 'ううう', 'ええええ'])
    expected = 'あ         a\nいい       bb\nううう     CCC\nええええ      D\ndtype: object'
    assert repr(s) == expected
    s = Series(['あ', 'いい', 'ううう', 'ええええ'], index=['a', 'bb', 'c', 'ddd'])
    expected = 'a         あ\nbb       いい\nc       ううう\nddd    ええええ\ndtype: object'
    assert repr(s) == expected
    s = Series(['あ', 'いい', 'ううう', 'ええええ'], index=['ああ', 'いいいい', 'う', 'えええ'])
    expected = 'ああ         あ\nいいいい      いい\nう        ううう\nえええ     ええええ\ndtype: object'
    assert repr(s) == expected
    s = Series(['あ', 'いい', 'ううう', 'ええええ'], index=['ああ', 'いいいい', 'う', 'えええ'], name='おおおおおおお')
    expected = 'ああ         あ\nいいいい      いい\nう        ううう\nえええ     ええええ\nName: おおおおおおお, dtype: object'
    assert repr(s) == expected
    idx = pd.MultiIndex.from_tuples([('あ', 'いい'), ('う', 'え'), ('おおお', 'かかかか'), ('き', 'くく')])
    s = Series([1, 22, 3333, 44444], index=idx)
    expected = 'あ    いい          1\nう    え          22\nおおお  かかかか     3333\nき    くく      44444\ndtype: int64'
    assert repr(s) == expected
    s = Series([1, 22, 3333, 44444], index=[1, 'AB', np.nan, 'あああ'])
    expected = '1          1\nAB        22\nNaN     3333\nあああ    44444\ndtype: int64'
    assert repr(s) == expected
    s = Series([1, 22, 3333, 44444], index=[1, 'AB', pd.Timestamp('2011-01-01'), 'あああ'])
    expected = '1                          1\nAB                        22\n2011-01-01 00:00:00     3333\nあああ                    44444\ndtype: int64'
    assert repr(s) == expected
    with option_context('display.max_rows', 3):
        s = Series(['あ', 'いい', 'ううう', 'ええええ'], name='おおおおおおお')
        expected = '0       あ\n     ... \n3    ええええ\nName: おおおおおおお, Length: 4, dtype: object'
        assert repr(s) == expected
        s.index = ['ああ', 'いいいい', 'う', 'えええ']
        expected = 'ああ        あ\n       ... \nえええ    ええええ\nName: おおおおおおお, Length: 4, dtype: object'
        assert repr(s) == expected
    with option_context('display.unicode.east_asian_width', True):
        s = Series(['a', 'bb', 'CCC', 'D'], index=['あ', 'いい', 'ううう', 'ええええ'])
        expected = 'あ            a\nいい         bb\nううう      CCC\nええええ      D\ndtype: object'
        assert repr(s) == expected
        s = Series(['あ', 'いい', 'ううう', 'ええええ'], index=['a', 'bb', 'c', 'ddd'])
        expected = 'a            あ\nbb         いい\nc        ううう\nddd    ええええ\ndtype: object'
        assert repr(s) == expected
        s = Series(['あ', 'いい', 'ううう', 'ええええ'], index=['ああ', 'いいいい', 'う', 'えええ'])
        expected = 'ああ              あ\nいいいい        いい\nう            ううう\nえええ      ええええ\ndtype: object'
        assert repr(s) == expected
        s = Series(['あ', 'いい', 'ううう', 'ええええ'], index=['ああ', 'いいいい', 'う', 'えええ'], name='おおおおおおお')
        expected = 'ああ              あ\nいいいい        いい\nう            ううう\nえええ      ええええ\nName: おおおおおおお, dtype: object'
        assert repr(s) == expected
        idx = pd.MultiIndex.from_tuples([('あ', 'いい'), ('う', 'え'), ('おおお', 'かかかか'), ('き', 'くく')])
        s = Series([1, 22, 3333, 44444], index=idx)
        expected = 'あ      いい            1\nう      え             22\nおおお  かかかか     3333\nき      くく        44444\ndtype: int64'
        assert repr(s) == expected
        s = Series([1, 22, 3333, 44444], index=[1, 'AB', np.nan, 'あああ'])
        expected = '1             1\nAB           22\nNaN        3333\nあああ    44444\ndtype: int64'
        assert repr(s) == expected
        s = Series([1, 22, 3333, 44444], index=[1, 'AB', pd.Timestamp('2011-01-01'), 'あああ'])
        expected = '1                          1\nAB                        22\n2011-01-01 00:00:00     3333\nあああ                 44444\ndtype: int64'
        assert repr(s) == expected
        with option_context('display.max_rows', 3):
            s = Series(['あ', 'いい', 'ううう', 'ええええ'], name='おおおおおおお')
            expected = '0          あ\n       ...   \n3    ええええ\nName: おおおおおおお, Length: 4, dtype: object'
            assert repr(s) == expected
            s.index = ['ああ', 'いいいい', 'う', 'えええ']
            expected = 'ああ            あ\n            ...   \nえええ    ええええ\nName: おおおおおおお, Length: 4, dtype: object'
            assert repr(s) == expected
        s = Series(['¡¡', 'い¡¡', 'ううう', 'ええええ'], index=['ああ', '¡¡¡¡いい', '¡¡', 'えええ'])
        expected = 'ああ              ¡¡\n¡¡¡¡いい        い¡¡\n¡¡            ううう\nえええ      ええええ\ndtype: object'
        assert repr(s) == expected