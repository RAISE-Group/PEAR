def read_dta(self, file):
    return read_stata(file, convert_dates=True)