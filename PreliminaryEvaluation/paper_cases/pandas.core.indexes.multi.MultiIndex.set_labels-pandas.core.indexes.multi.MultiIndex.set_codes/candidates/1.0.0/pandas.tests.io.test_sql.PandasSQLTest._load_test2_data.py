def _load_test2_data(self):
    df = DataFrame(dict(A=[4, 1, 3, 6], B=['asd', 'gsq', 'ylt', 'jkl'], C=[1.1, 3.1, 6.9, 5.3], D=[False, True, True, False], E=['1990-11-22', '1991-10-26', '1993-11-26', '1995-12-12']))
    df['E'] = to_datetime(df['E'])
    self.test_frame2 = df