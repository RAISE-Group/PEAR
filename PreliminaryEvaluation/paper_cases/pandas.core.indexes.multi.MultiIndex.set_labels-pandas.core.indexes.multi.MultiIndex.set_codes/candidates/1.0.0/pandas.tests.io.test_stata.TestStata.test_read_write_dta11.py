def test_read_write_dta11(self):
    original = DataFrame([(1, 2, 3, 4)], columns=['good', 'bäd', '8number', 'astringwithmorethan32characters______'])
    formatted = DataFrame([(1, 2, 3, 4)], columns=['good', 'b_d', '_8number', 'astringwithmorethan32characters_'])
    formatted.index.name = 'index'
    formatted = formatted.astype(np.int32)
    with tm.ensure_clean() as path:
        with tm.assert_produces_warning(pd.io.stata.InvalidColumnName):
            original.to_stata(path, None)
        written_and_read_again = self.read_dta(path)
        tm.assert_frame_equal(written_and_read_again.set_index('index'), formatted)