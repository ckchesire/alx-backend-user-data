---

#  Secure Logging and Authentication Guide

This guide covers secure handling of sensitive data in Python applications.

---

##  Examples of PII (Personally Identifiable Information)

* Full name, email, phone number
* Social Security Number (SSN), passport ID
* Passwords, bank account or credit card numbers
* Medical or biometric data

---

## Log Filtering to Obfuscate PII

Use a custom logging filter with regex to mask PII fields in log messages.

```python
# Example obfuscation: "email=***; password=***"
```

---

## Password Hashing & Validation

Use `bcrypt` to securely hash and verify passwords.

```python
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
bcrypt.checkpw(input_password.encode(), hashed)
```

---

## DB Authentication Using Environment Variables

Connect to databases without hardcoding credentials:

```python
import os
os.getenv("DB_USER")  # Securely fetch DB credentials
```

Set your environment:

```bash
export DB_USER=username
export DB_PASSWORD=secret
```

---

## Best Practices

* Always obfuscate logs that may contain PII.
* Never store plain-text passwords—use bcrypt.
* Load sensitive configs using environment variables, not in source code.
