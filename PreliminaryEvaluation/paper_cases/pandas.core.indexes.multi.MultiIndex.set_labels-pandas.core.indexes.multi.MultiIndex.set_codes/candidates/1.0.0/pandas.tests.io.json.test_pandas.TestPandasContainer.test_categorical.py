def test_categorical(self):
    df = DataFrame({'A': ['a', 'b', 'c', 'a', 'b', 'b', 'a']})
    df['B'] = df['A']
    expected = df.to_json()
    df['B'] = df['A'].astype('category')
    assert expected == df.to_json()
    s = df['A']
    sc = df['B']
    assert s.to_json() == sc.to_json()