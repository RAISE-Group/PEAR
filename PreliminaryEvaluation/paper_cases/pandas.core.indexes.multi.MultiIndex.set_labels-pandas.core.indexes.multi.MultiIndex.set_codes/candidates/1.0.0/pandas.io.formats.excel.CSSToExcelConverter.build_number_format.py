def build_number_format(self, props: Dict) -> Dict[str, Optional[str]]:
    return {'format_code': props.get('number-format')}