def test_warning_case_insensitive_table_name(self):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        self.test_frame1.to_sql('CaseSensitive', self.conn)
        assert len(w) == 0