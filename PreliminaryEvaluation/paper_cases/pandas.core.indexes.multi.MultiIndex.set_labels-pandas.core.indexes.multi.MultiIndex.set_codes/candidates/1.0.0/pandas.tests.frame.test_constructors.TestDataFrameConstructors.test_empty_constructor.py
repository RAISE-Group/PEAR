@pytest.mark.parametrize('constructor', [lambda: DataFrame(), lambda: DataFrame(None), lambda: DataFrame({}), lambda: DataFrame(()), lambda: DataFrame([]), lambda: DataFrame((_ for _ in [])), lambda: DataFrame(range(0)), lambda: DataFrame(data=None), lambda: DataFrame(data={}), lambda: DataFrame(data=()), lambda: DataFrame(data=[]), lambda: DataFrame(data=(_ for _ in [])), lambda: DataFrame(data=range(0))])
def test_empty_constructor(self, constructor):
    expected = DataFrame()
    result = constructor()
    assert len(result.index) == 0
    assert len(result.columns) == 0
    tm.assert_frame_equal(result, expected)