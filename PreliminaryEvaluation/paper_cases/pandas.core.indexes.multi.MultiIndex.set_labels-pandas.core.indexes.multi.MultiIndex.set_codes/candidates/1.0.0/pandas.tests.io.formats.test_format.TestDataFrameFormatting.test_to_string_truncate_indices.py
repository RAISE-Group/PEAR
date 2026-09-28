def test_to_string_truncate_indices(self):
    for index in [tm.makeStringIndex, tm.makeUnicodeIndex, tm.makeIntIndex, tm.makeDateIndex, tm.makePeriodIndex]:
        for column in [tm.makeStringIndex]:
            for h in [10, 20]:
                for w in [10, 20]:
                    with option_context('display.expand_frame_repr', False):
                        df = DataFrame(index=index(h), columns=column(w))
                        with option_context('display.max_rows', 15):
                            if h == 20:
                                assert has_vertically_truncated_repr(df)
                            else:
                                assert not has_vertically_truncated_repr(df)
                        with option_context('display.max_columns', 15):
                            if w == 20:
                                assert has_horizontally_truncated_repr(df)
                            else:
                                assert not has_horizontally_truncated_repr(df)
                        with option_context('display.max_rows', 15, 'display.max_columns', 15):
                            if h == 20 and w == 20:
                                assert has_doubly_truncated_repr(df)
                            else:
                                assert not has_doubly_truncated_repr(df)