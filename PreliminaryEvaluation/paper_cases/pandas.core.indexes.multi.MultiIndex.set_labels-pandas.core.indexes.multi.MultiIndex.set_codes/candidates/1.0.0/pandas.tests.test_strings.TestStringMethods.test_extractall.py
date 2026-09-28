def test_extractall(self):
    subject_list = ['dave@google.com', 'tdhock5@gmail.com', 'maudelaperriere@gmail.com', 'rob@gmail.com some text steve@gmail.com', 'a@b.com some text c@d.com and e@f.com', np.nan, '']
    expected_tuples = [('dave', 'google', 'com'), ('tdhock5', 'gmail', 'com'), ('maudelaperriere', 'gmail', 'com'), ('rob', 'gmail', 'com'), ('steve', 'gmail', 'com'), ('a', 'b', 'com'), ('c', 'd', 'com'), ('e', 'f', 'com')]
    named_pattern = '\n        (?P<user>[a-z0-9]+)\n        @\n        (?P<domain>[a-z]+)\n        \\.\n        (?P<tld>[a-z]{2,4})\n        '
    expected_columns = ['user', 'domain', 'tld']
    S = Series(subject_list)
    expected_index = MultiIndex.from_tuples([(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 0), (4, 1), (4, 2)], names=(None, 'match'))
    expected_df = DataFrame(expected_tuples, expected_index, expected_columns)
    computed_df = S.str.extractall(named_pattern, re.VERBOSE)
    tm.assert_frame_equal(computed_df, expected_df)
    series_index = MultiIndex.from_tuples([('single', 'Dave'), ('single', 'Toby'), ('single', 'Maude'), ('multiple', 'robAndSteve'), ('multiple', 'abcdef'), ('none', 'missing'), ('none', 'empty')])
    Si = Series(subject_list, series_index)
    expected_index = MultiIndex.from_tuples([('single', 'Dave', 0), ('single', 'Toby', 0), ('single', 'Maude', 0), ('multiple', 'robAndSteve', 0), ('multiple', 'robAndSteve', 1), ('multiple', 'abcdef', 0), ('multiple', 'abcdef', 1), ('multiple', 'abcdef', 2)], names=(None, None, 'match'))
    expected_df = DataFrame(expected_tuples, expected_index, expected_columns)
    computed_df = Si.str.extractall(named_pattern, re.VERBOSE)
    tm.assert_frame_equal(computed_df, expected_df)
    Sn = Series(subject_list, series_index)
    Sn.index.names = ('matches', 'description')
    expected_index.names = ('matches', 'description', 'match')
    expected_df = DataFrame(expected_tuples, expected_index, expected_columns)
    computed_df = Sn.str.extractall(named_pattern, re.VERBOSE)
    tm.assert_frame_equal(computed_df, expected_df)
    subject_list = ['', 'A1', '32']
    named_pattern = '(?P<letter>[AB])?(?P<number>[123])'
    computed_df = Series(subject_list).str.extractall(named_pattern)
    expected_index = MultiIndex.from_tuples([(1, 0), (2, 0), (2, 1)], names=(None, 'match'))
    expected_df = DataFrame([('A', '1'), (np.nan, '3'), (np.nan, '2')], expected_index, columns=['letter', 'number'])
    tm.assert_frame_equal(computed_df, expected_df)
    pattern = '([AB])?(?P<number>[123])'
    computed_df = Series(subject_list).str.extractall(pattern)
    expected_df = DataFrame([('A', '1'), (np.nan, '3'), (np.nan, '2')], expected_index, columns=[0, 'number'])
    tm.assert_frame_equal(computed_df, expected_df)