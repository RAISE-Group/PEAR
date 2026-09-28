def _get_monthly_rule(self) -> Optional[str]:
    if len(self.mdiffs) > 1:
        return None
    pos_check = self.month_position_check()
    return {'cs': 'MS', 'bs': 'BMS', 'ce': 'M', 'be': 'BM'}.get(pos_check)