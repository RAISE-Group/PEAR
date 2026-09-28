def test_validation(self):
    left = DataFrame({'a': ['a', 'b', 'c', 'd'], 'b': ['cat', 'dog', 'weasel', 'horse']}, index=range(4))
    right = DataFrame({'a': ['a', 'b', 'c', 'd', 'e'], 'c': ['meow', 'bark', 'um... weasel noise?', 'nay', 'chirp']}, index=range(5))
    left_copy = left.copy()
    right_copy = right.copy()
    result = merge(left, right, left_index=True, right_index=True, validate='1:1')
    tm.assert_frame_equal(left, left_copy)
    tm.assert_frame_equal(right, right_copy)
    expected = DataFrame({'a_x': ['a', 'b', 'c', 'd'], 'b': ['cat', 'dog', 'weasel', 'horse'], 'a_y': ['a', 'b', 'c', 'd'], 'c': ['meow', 'bark', 'um... weasel noise?', 'nay']}, index=range(4), columns=['a_x', 'b', 'a_y', 'c'])
    result = merge(left, right, left_index=True, right_index=True, validate='one_to_one')
    tm.assert_frame_equal(result, expected)
    expected_2 = DataFrame({'a': ['a', 'b', 'c', 'd'], 'b': ['cat', 'dog', 'weasel', 'horse'], 'c': ['meow', 'bark', 'um... weasel noise?', 'nay']}, index=range(4))
    result = merge(left, right, on='a', validate='1:1')
    tm.assert_frame_equal(left, left_copy)
    tm.assert_frame_equal(right, right_copy)
    tm.assert_frame_equal(result, expected_2)
    result = merge(left, right, on='a', validate='one_to_one')
    tm.assert_frame_equal(result, expected_2)
    expected_3 = DataFrame({'b': ['cat', 'dog', 'weasel', 'horse'], 'a': ['a', 'b', 'c', 'd'], 'c': ['meow', 'bark', 'um... weasel noise?', 'nay']}, columns=['b', 'a', 'c'], index=range(4))
    left_index_reset = left.set_index('a')
    result = merge(left_index_reset, right, left_index=True, right_on='a', validate='one_to_one')
    tm.assert_frame_equal(result, expected_3)
    right_w_dups = right.append(pd.DataFrame({'a': ['e'], 'c': ['moo']}, index=[4]))
    merge(left, right_w_dups, left_index=True, right_index=True, validate='one_to_many')
    msg = 'Merge keys are not unique in right dataset; not a one-to-one merge'
    with pytest.raises(MergeError, match=msg):
        merge(left, right_w_dups, left_index=True, right_index=True, validate='one_to_one')
    with pytest.raises(MergeError, match=msg):
        merge(left, right_w_dups, on='a', validate='one_to_one')
    left_w_dups = left.append(pd.DataFrame({'a': ['a'], 'c': ['cow']}, index=[3]), sort=True)
    merge(left_w_dups, right, left_index=True, right_index=True, validate='many_to_one')
    msg = 'Merge keys are not unique in left dataset; not a one-to-one merge'
    with pytest.raises(MergeError, match=msg):
        merge(left_w_dups, right, left_index=True, right_index=True, validate='one_to_one')
    with pytest.raises(MergeError, match=msg):
        merge(left_w_dups, right, on='a', validate='one_to_one')
    merge(left_w_dups, right_w_dups, on='a', validate='many_to_many')
    msg = 'Merge keys are not unique in right dataset; not a many-to-one merge'
    with pytest.raises(MergeError, match=msg):
        merge(left_w_dups, right_w_dups, left_index=True, right_index=True, validate='many_to_one')
    msg = 'Merge keys are not unique in left dataset; not a one-to-many merge'
    with pytest.raises(MergeError, match=msg):
        merge(left_w_dups, right_w_dups, on='a', validate='one_to_many')
    msg = 'Not a valid argument for validate'
    with pytest.raises(ValueError, match=msg):
        merge(left, right, on='a', validate='jibberish')
    left = DataFrame({'a': ['a', 'a', 'b', 'b'], 'b': [0, 1, 0, 1], 'c': ['cat', 'dog', 'weasel', 'horse']}, index=range(4))
    right = DataFrame({'a': ['a', 'a', 'b'], 'b': [0, 1, 0], 'd': ['meow', 'bark', 'um... weasel noise?']}, index=range(3))
    expected_multi = DataFrame({'a': ['a', 'a', 'b'], 'b': [0, 1, 0], 'c': ['cat', 'dog', 'weasel'], 'd': ['meow', 'bark', 'um... weasel noise?']}, index=range(3))
    msg = 'Merge keys are not unique in either left or right dataset; not a one-to-one merge'
    with pytest.raises(MergeError, match=msg):
        merge(left, right, on='a', validate='1:1')
    result = merge(left, right, on=['a', 'b'], validate='1:1')
    tm.assert_frame_equal(result, expected_multi)