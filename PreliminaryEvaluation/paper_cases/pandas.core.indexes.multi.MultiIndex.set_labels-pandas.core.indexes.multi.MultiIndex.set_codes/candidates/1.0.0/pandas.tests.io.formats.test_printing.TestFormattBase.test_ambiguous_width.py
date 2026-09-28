def test_ambiguous_width(self):
    adj = fmt.EastAsianTextAdjustment()
    assert adj.len('¡¡ab') == 4
    with cf.option_context('display.unicode.ambiguous_as_wide', True):
        adj = fmt.EastAsianTextAdjustment()
        assert adj.len('¡¡ab') == 6
    data = [['あ', 'b', 'c'], ['dd', 'ええ', 'ff'], ['ggg', '¡¡ab', 'いいい']]
    expected = 'あ  dd    ggg \nb   ええ  ¡¡ab\nc   ff    いいい'
    adjoined = adj.adjoin(2, *data)
    assert adjoined == expected