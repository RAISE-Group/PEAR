@cache_readonly
def is_monotonic(self) -> bool:
    return Index(self.group_info[0]).is_monotonic