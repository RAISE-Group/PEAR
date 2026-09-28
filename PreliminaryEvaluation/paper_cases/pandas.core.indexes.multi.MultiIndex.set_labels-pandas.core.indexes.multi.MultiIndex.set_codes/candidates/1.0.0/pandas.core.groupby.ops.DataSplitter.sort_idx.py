@cache_readonly
def sort_idx(self):
    return get_group_index_sorter(self.labels, self.ngroups)