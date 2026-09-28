def test_hide_multiindex(self):
    df = pd.DataFrame({'A': [1, 2]}, index=pd.MultiIndex.from_arrays([['a', 'a'], [0, 1]], names=['idx_level_0', 'idx_level_1']))
    ctx1 = df.style._translate()
    assert ctx1['body'][0][0]['is_visible']
    assert ctx1['body'][0][1]['is_visible']
    assert ctx1['head'][0][0]['is_visible']
    assert ctx1['head'][0][1]['is_visible']
    ctx2 = df.style.hide_index()._translate()
    assert not ctx2['body'][0][0]['is_visible']
    assert not ctx2['body'][0][1]['is_visible']
    assert not ctx2['head'][0][0]['is_visible']
    assert not ctx2['head'][0][1]['is_visible']