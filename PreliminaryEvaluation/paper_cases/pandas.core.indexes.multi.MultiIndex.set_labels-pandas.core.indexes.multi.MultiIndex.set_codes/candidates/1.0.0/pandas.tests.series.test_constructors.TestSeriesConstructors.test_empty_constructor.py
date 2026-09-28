@pytest.mark.parametrize('constructor,check_index_type', [(lambda: Series(), True), (lambda: Series(None), True), (lambda: Series({}), True), (lambda: Series(()), False), (lambda: Series([]), False), (lambda: Series((_ for _ in [])), False), (lambda: Series(data=None), True), (lambda: Series(data={}), True), (lambda: Series(data=()), False), (lambda: Series(data=[]), False), (lambda: Series(data=(_ for _ in [])), False)])
def test_empty_constructor(self, constructor, check_index_type):
    with tm.assert_produces_warning(DeprecationWarning, check_stacklevel=False):
        expected = Series()
        result = constructor()
    assert len(result.index) == 0
    tm.assert_series_equal(result, expected, check_index_type=check_index_type)