#!/usr/bin/env python3
""" Main 1
"""
from api.v1.auth.auth import Auth

a = Auth()

print(a.require_auth("/api/v1/users/", ["/api/v1/stat*"]))
print(a.require_auth("/api/v1/status", ["/api/v1/stat*"]))
print(a.require_auth("/api/v1/stats", ["/api/v1/stat*"]))
