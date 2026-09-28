@pytest.mark.parametrize('scalar', [2, np.nan, None, 'D'])
def test_constructor_invalid_items_unused(self, scalar):
    result = DataFrame({'a': scalar}, columns=['b'])
    expected = DataFrame(columns=['b'])
    tm.assert_frame_equal(result, expected)