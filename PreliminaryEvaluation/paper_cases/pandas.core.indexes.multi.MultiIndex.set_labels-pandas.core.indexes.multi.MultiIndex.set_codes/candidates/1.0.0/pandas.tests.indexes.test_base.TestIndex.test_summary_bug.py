def test_summary_bug(self):
    ind = Index(['{other}%s', '~:{range}:0'], name='A')
    result = ind._summary()
    assert '~:{range}:0' in result
    assert '{other}%s' in result