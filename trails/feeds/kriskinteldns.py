#!/usr/bin/env python

"""
Copyright (c) 2014-2020 Maltrail developers (https://github.com/stamparm/maltrail/)
See the file 'LICENSE' for copying permission
"""

from core.common import retrieve_content

__url__ = "https://kriskintel.com/feeds/ktip_malicious_domains.txt"
__check__ = "Feed last refreshed at"
__info__ = "malicious"
__reference__ = "kriskintel.com"

def fetch():
    retval = {}
    content = retrieve_content(__url__)

    if __check__ in content:
        for line in content.split('\n'):
            line = line.strip()
            if not line or line.startswith('#') or '.' not in line:
                continue
            retval[line] = (__info__, __reference__)

    return retval
