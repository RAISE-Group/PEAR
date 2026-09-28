def test_validate_ordered(self):
    exp_msg = "'ordered' must either be 'True' or 'False'"
    exp_err = TypeError
    ordered = np.array([0, 1, 2])
    with pytest.raises(exp_err, match=exp_msg):
        Categorical([1, 2, 3], ordered=ordered)
    with pytest.raises(exp_err, match=exp_msg):
        Categorical.from_codes([0, 0, 1], categories=['a', 'b', 'c'], ordered=ordered)