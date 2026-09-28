def test_unicode_problem_decoding_as_ascii(self):
    dm = DataFrame({'c/σ': Series({'test': np.nan})})
    str(dm.to_string())