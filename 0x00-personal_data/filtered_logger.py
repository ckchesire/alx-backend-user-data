#!/usr/bin/env python3
"""
This module filters and obfuscates senisitive log fields using regex.
"""


import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """
    Function to obfusacte values of specific fields in a log message.

    Args:
        fields: list of field names to redact
        redaction: string to replace the specified fields
        message: log message string
        separator: character seperating fields in the log

    Returns:
        Obfuscated log message is returned as output.
    """
    return re.sub(
            rf'({"|".join(fields)})=[^ {separator}]*',
            lambda m: f"{m.group(1)}={redaction}",
            message
            )
