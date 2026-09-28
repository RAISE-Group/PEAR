def create_index(self, closed='right'):
    return IntervalIndex.from_breaks(range(11), closed=closed)