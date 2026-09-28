@pytest.mark.parametrize('kwarg', [dict(left_index=True, right_index=True), dict(left_index=True, right_on='x'), dict(left_on='a', right_index=True), dict(left_on='a', right_on='x')])
def test_merge_left_empty_right_empty(self, join_type, kwarg):
    left = pd.DataFrame(columns=['a', 'b', 'c'])
    right = pd.DataFrame(columns=['x', 'y', 'z'])
    exp_in = pd.DataFrame(columns=['a', 'b', 'c', 'x', 'y', 'z'], index=pd.Index([], dtype=object), dtype=object)
    result = pd.merge(left, right, how=join_type, **kwarg)
    tm.assert_frame_equal(result, exp_in)