#!/usr/bin/env python3
"""
This module filters and obfuscates senisitive log fields using regex.
"""


import re
import os
import logging
from typing import List
import mysql.connector
from mysql.connector.connection import MySQLConnection


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_db() -> MySQLConnection:
    """
    Uses environment variables to connect securely to the MySQL database.

    Returns:
        MySQLConnection: A connection object to the database
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=database
            )


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


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""
    REDACTION = "***"
    FRMT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initializes the formatter with specific fields to redact
        """
        super(RedactingFormatter, self).__init__(self.FRMT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Apply filtering to log message
        """
        original = super().format(record)
        return filter_datum(
                self.fields,
                self.REDACTION,
                original,
                self.SEPARATOR
                )


def get_logger() -> logging.Logger:
    """
    Returns a logger configured to redact PII fields in user data
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


def main():
    """
    Main function that retrieves data from users table and logs each row with
    sensitive fields redacted.
    """
    db = get_db()
    cursor = db.cursor()

    query = "SELECT * FROM users;"
    cursor.execute(query)

    field_names = [i[0] for i in cursor.description]
    logger = get_logger()

    for row in cursor:
        row_dict = dict(zip(field_names, row))
        message = "; ".join(f"{k}={v}" for k, v in row_dict.items()) + ";"
        logger.info(message)

    cursor.close()
    db.close()
