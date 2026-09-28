def test_merge_datatype_categorical_error_raises(self):
    msg = 'incompatible merge keys \\[0\\] .* both sides category, but not equal ones'
    left = pd.DataFrame({'left_val': [1, 5, 10], 'a': pd.Categorical(['a', 'b', 'c'])})
    right = pd.DataFrame({'right_val': [1, 2, 3, 6, 7], 'a': pd.Categorical(['a', 'X', 'c', 'X', 'b'])})
    with pytest.raises(MergeError, match=msg):
        merge_asof(left, right, on='a')