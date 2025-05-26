# Authentication and Basic Auth with Base64

## What is Authentication?

**Authentication** is the process of verifying the identity of a user or system. In web applications, authentication ensures that a user is who they claim to be—typically using credentials like usernames, passwords, or tokens.

## What is Basic Authentication?

**Basic Authentication** is a simple HTTP authentication scheme in which the client sends a username and password with each request. The credentials are encoded using **Base64** and included in the request's `Authorization` header.

- It follows this format:
```

Authorization: Basic \<Base64(username\:password)>

```

> Basic Auth is not secure on its own and should only be used over HTTPS.


## What is Base64?

**Base64** is a method of encoding binary data into a text format using ASCII characters. It is commonly used to encode credentials or binary data in email, HTTP headers, or URLs.

- Base64 does **not** encrypt or secure data—it only encodes it in a readable format.

## How to Encode a String in Base64

To encode a string like `username:password` into Base64:

### Using Python
```python
import base64

credentials = "username:password"
encoded = base64.b64encode(credentials.encode()).decode()
print(encoded)
```

## How to Send the Authorization Header

After encoding your credentials, include them in the HTTP `Authorization` header:

### Example with `curl`

```bash
curl -H "Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=" https://api.example.com/secure-data
```

### Example in HTTP request format

```
GET /secure-data HTTP/1.1
Host: api.example.com
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
```


## Summary

* Authentication verifies identity.
* Basic Auth uses Base64 to encode `username:password`.
* Base64 is not encryption—use HTTPS to secure the transmission.
* The Authorization header follows the format:

  ```
  Authorization: Basic <Base64(username:password)>
  ```