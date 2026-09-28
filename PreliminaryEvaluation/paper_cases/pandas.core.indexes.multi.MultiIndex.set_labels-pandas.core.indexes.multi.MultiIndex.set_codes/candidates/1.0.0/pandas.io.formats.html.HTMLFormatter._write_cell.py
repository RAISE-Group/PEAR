def _write_cell(self, s: Any, kind: str='td', indent: int=0, tags: Optional[str]=None) -> None:
    if tags is not None:
        start_tag = '<{kind} {tags}>'.format(kind=kind, tags=tags)
    else:
        start_tag = '<{kind}>'.format(kind=kind)
    if self.escape:
        esc = {'&': '&amp;', '<': '&lt;', '>': '&gt;'}
    else:
        esc = {}
    rs = pprint_thing(s, escape_chars=esc).strip()
    if self.render_links and is_url(rs):
        rs_unescaped = pprint_thing(s, escape_chars={}).strip()
        start_tag += '<a href="{url}" target="_blank">'.format(url=rs_unescaped)
        end_a = '</a>'
    else:
        end_a = ''
    self.write('{start}{rs}{end_a}</{kind}>'.format(start=start_tag, rs=rs, end_a=end_a, kind=kind), indent)