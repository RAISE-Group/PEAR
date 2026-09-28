def _get_quarterly_rule(self) -> Optional[str]:
    if len(self.mdiffs) > 1:
        return None
    if not self.mdiffs[0] % 3 == 0:
        return None
    pos_check = self.month_position_check()
    return {'cs': 'QS', 'bs': 'BQS', 'ce': 'Q', 'be': 'BQ'}.get(pos_check)