def test_sample(sel):
    easy_weight_list = [0] * 10
    easy_weight_list[5] = 1
    df = pd.DataFrame({'col1': range(10, 20), 'col2': range(20, 30), 'colString': ['a'] * 10, 'easyweights': easy_weight_list})
    sample1 = df.sample(n=1, weights='easyweights')
    tm.assert_frame_equal(sample1, df.iloc[5:6])
    s = Series(range(10))
    with pytest.raises(ValueError):
        s.sample(n=3, weights='weight_column')
    with pytest.raises(ValueError):
        df.sample(n=1, weights='weight_column', axis=1)
    with pytest.raises(KeyError, match="'String passed to weights not a valid column'"):
        df.sample(n=3, weights='not_a_real_column_name')
    weights_less_than_1 = [0] * 10
    weights_less_than_1[0] = 0.5
    tm.assert_frame_equal(df.sample(n=1, weights=weights_less_than_1), df.iloc[:1])
    df = pd.DataFrame({'col1': range(10), 'col2': ['a'] * 10})
    second_column_weight = [0, 1]
    tm.assert_frame_equal(df.sample(n=1, axis=1, weights=second_column_weight), df[['col2']])
    tm.assert_frame_equal(df.sample(n=1, axis='columns', weights=second_column_weight), df[['col2']])
    weight = [0] * 10
    weight[5] = 0.5
    tm.assert_frame_equal(df.sample(n=1, axis='rows', weights=weight), df.iloc[5:6])
    tm.assert_frame_equal(df.sample(n=1, axis='index', weights=weight), df.iloc[5:6])
    with pytest.raises(ValueError):
        df.sample(n=1, axis=2)
    with pytest.raises(ValueError):
        df.sample(n=1, axis='not_a_name')
    with pytest.raises(ValueError):
        s = pd.Series(range(10))
        s.sample(n=1, axis=1)
    with pytest.raises(ValueError):
        df.sample(n=1, axis=1, weights=[0.5] * 10)
    easy_weight_list = [0] * 3
    easy_weight_list[2] = 1
    df = pd.DataFrame({'col1': range(10, 20), 'col2': range(20, 30), 'colString': ['a'] * 10})
    sample1 = df.sample(n=1, axis=1, weights=easy_weight_list)
    tm.assert_frame_equal(sample1, df[['colString']])
    tm.assert_frame_equal(df.sample(n=3, random_state=42), df.sample(n=3, axis=0, random_state=42))
    df = DataFrame({'col1': [5, 6, 7], 'col2': ['a', 'b', 'c']}, index=[9, 5, 3])
    s = Series([1, 0, 0], index=[3, 5, 9])
    tm.assert_frame_equal(df.loc[[3]], df.sample(1, weights=s))
    s2 = Series([0.001, 0, 10000], index=[3, 5, 10])
    tm.assert_frame_equal(df.loc[[3]], df.sample(1, weights=s2))
    s3 = Series([0.01, 0], index=[3, 5])
    tm.assert_frame_equal(df.loc[[3]], df.sample(1, weights=s3))
    s4 = Series([1, 0], index=[1, 2])
    with pytest.raises(ValueError):
        df.sample(1, weights=s4)