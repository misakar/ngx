import re
# 127.0.0.1 - - [15/Nov/2016:00:39:52 +0800] "GET /nginx_status/ HTTP/1.1" 200 112 "-" "Cloudinsight Agent/4.7.2"

log_patterns = r'(\S+) (\S+) (\S+) \[(.*?)\] "(\S+) (\S+) (\S+)" (\S+) (\S+) "(\S+)" "(\S+) (\S+)"'
log_pattern = re.compile(log_patterns)

def handle(lines):
    items = (
        'remote_addr', '-', 'remote_user', 'time_local', 'request_method',
        'request_path', 'request_protocol', 'request_status', 'body_bytes_sent',
        '-', 'http_referer', 'http_user_agent'
    )
    groups = (log_pattern.match(line) for line in lines)
    tuples = (g.groups() for g in groups if g)
    log_dict = (dict(zip(items, t)) for t in tuples)
    return log_dict
