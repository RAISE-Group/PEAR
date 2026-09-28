@pytest.mark.parametrize('result_rows,result_columns,index_product,expected_row', [([[1, 1, None, None, 30.0, None], [2, 2, None, None, 30.0, None]], ['ix1', 'ix2', 'col1', 'col2', 'col3', 'col4'], 2, [None, None, 30.0, None]), ([[1, 1, None, None, 30.0], [2, 2, None, None, 30.0]], ['ix1', 'ix2', 'col1', 'col2', 'col3'], 2, [None, None, 30.0]), ([[1, 1, None, None, 30.0], [2, None, None, None, 30.0]], ['ix1', 'ix2', 'col1', 'col2', 'col3'], None, [None, None, 30.0])])
def test_unstack_partial(self, result_rows, result_columns, index_product, expected_row):
    result = pd.DataFrame(result_rows, columns=result_columns).set_index(['ix1', 'ix2'])
    result = result.iloc[1:2].unstack('ix2')
    expected = pd.DataFrame([expected_row], columns=pd.MultiIndex.from_product([result_columns[2:], [index_product]], names=[None, 'ix2']), index=pd.Index([2], name='ix1'))
    tm.assert_frame_equal(result, expected)