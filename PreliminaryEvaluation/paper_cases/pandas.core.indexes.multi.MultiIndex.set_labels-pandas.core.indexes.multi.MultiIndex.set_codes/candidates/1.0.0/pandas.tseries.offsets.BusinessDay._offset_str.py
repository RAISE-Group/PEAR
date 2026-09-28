def _offset_str(self):

    def get_str(td):
        off_str = ''
        if td.days > 0:
            off_str += str(td.days) + 'D'
        if td.seconds > 0:
            s = td.seconds
            hrs = int(s / 3600)
            if hrs != 0:
                off_str += str(hrs) + 'H'
                s -= hrs * 3600
            mts = int(s / 60)
            if mts != 0:
                off_str += str(mts) + 'Min'
                s -= mts * 60
            if s != 0:
                off_str += str(s) + 's'
        if td.microseconds > 0:
            off_str += str(td.microseconds) + 'us'
        return off_str
    if isinstance(self.offset, timedelta):
        zero = timedelta(0, 0, 0)
        if self.offset >= zero:
            off_str = '+' + get_str(self.offset)
        else:
            off_str = '-' + get_str(-self.offset)
        return off_str
    else:
        return '+' + repr(self.offset)