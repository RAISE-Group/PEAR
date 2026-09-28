def test_merge_datatype_error_raises(self):
    msg = 'incompatible merge keys \\[0\\] .*, must be the same type'
    left = pd.DataFrame({'left_val': [1, 5, 10], 'a': ['a', 'b', 'c']})
    right = pd.DataFrame({'right_val': [1, 2, 3, 6, 7], 'a': [1, 2, 3, 6, 7]})
    with pytest.raises(MergeError, match=msg):
        merge_asof(left, right, on='a')