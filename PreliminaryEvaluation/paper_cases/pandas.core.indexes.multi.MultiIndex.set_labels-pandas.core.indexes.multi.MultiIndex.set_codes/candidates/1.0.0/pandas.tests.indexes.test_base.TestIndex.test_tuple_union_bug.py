@pytest.mark.parametrize('method,expected,sort', [('intersection', np.array([(1, 'A'), (2, 'A'), (1, 'B'), (2, 'B')], dtype=[('num', int), ('let', 'a1')]), False), ('intersection', np.array([(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')], dtype=[('num', int), ('let', 'a1')]), None), ('union', np.array([(1, 'A'), (1, 'B'), (1, 'C'), (2, 'A'), (2, 'B'), (2, 'C')], dtype=[('num', int), ('let', 'a1')]), None)])
def test_tuple_union_bug(self, method, expected, sort):
    index1 = Index(np.array([(1, 'A'), (2, 'A'), (1, 'B'), (2, 'B')], dtype=[('num', int), ('let', 'a1')]))
    index2 = Index(np.array([(1, 'A'), (2, 'A'), (1, 'B'), (2, 'B'), (1, 'C'), (2, 'C')], dtype=[('num', int), ('let', 'a1')]))
    result = getattr(index1, method)(index2, sort=sort)
    assert result.ndim == 1
    expected = Index(expected)
    tm.assert_index_equal(result, expected)