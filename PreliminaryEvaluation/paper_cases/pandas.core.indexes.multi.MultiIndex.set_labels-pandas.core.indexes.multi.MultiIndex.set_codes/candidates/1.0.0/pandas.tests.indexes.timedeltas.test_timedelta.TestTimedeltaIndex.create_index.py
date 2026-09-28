def create_index(self):
    return pd.to_timedelta(range(5), unit='d') + pd.offsets.Hour(1)