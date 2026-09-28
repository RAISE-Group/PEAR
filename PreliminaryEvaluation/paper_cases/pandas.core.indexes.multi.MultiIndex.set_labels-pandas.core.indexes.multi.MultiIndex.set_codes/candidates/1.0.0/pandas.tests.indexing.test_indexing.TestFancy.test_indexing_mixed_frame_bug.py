def test_indexing_mixed_frame_bug(self):
    df = DataFrame({'a': {1: 'aaa', 2: 'bbb', 3: 'ccc'}, 'b': {1: 111, 2: 222, 3: 333}})
    df['test'] = df['a'].apply(lambda x: '_' if x == 'aaa' else x)
    idx = df['test'] == '_'
    temp = df.loc[idx, 'a'].apply(lambda x: '-----' if x == 'aaa' else x)
    df.loc[idx, 'test'] = temp
    assert df.iloc[0, 2] == '-----'