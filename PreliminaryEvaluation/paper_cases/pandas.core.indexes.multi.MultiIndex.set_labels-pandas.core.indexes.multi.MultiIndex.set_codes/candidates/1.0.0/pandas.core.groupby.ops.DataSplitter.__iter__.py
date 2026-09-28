def __iter__(self):
    sdata = self._get_sorted_data()
    if self.ngroups == 0:
        return
    starts, ends = lib.generate_slices(self.slabels, self.ngroups)
    for i, (start, end) in enumerate(zip(starts, ends)):
        yield (i, self._chop(sdata, slice(start, end)))