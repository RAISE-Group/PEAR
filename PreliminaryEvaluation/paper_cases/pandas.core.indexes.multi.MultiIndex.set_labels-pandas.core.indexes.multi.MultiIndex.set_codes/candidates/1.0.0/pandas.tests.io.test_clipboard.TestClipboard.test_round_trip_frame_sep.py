@pytest.mark.parametrize('sep', ['\t', ',', '|'])
def test_round_trip_frame_sep(self, df, sep):
    self.check_round_trip_frame(df, sep=sep)