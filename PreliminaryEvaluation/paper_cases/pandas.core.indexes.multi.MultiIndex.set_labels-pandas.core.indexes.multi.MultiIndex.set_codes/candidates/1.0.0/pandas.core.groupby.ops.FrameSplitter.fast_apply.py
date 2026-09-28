def fast_apply(self, f, names):
    starts, ends = lib.generate_slices(self.slabels, self.ngroups)
    sdata = self._get_sorted_data()
    return libreduction.apply_frame_axis0(sdata, f, names, starts, ends)