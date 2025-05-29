# Web Authentication and Cookies Overview

The following is a concise explanation of key concepts in web authentication and cookie management, essential for understanding how sessions and identity are handled in web applications.

## 1. What is Authentication?

Authentication is the process of verifying the identity of a user or system. It answers the question: **"Who are you?"**

Common authentication methods:
- Username and password
- API keys
- JSON Web Tokens (JWT)
- OAuth tokens

Example:
A user enters a username and password. The server verifies the credentials. If they match, the user is authenticated.

## 2. What is Session Authentication?

Session authentication involves maintaining the authentication state on the server.

**How it works:**
1. The user logs in with valid credentials.
2. The server creates a session and stores the user's session ID (usually in memory or a database).
3. The server sends the session ID to the client in a cookie.
4. The client sends the cookie with each request.
5. The server uses the session ID to verify the user's identity.

## 3. What are Cookies?

Cookies are small pieces of data stored on the client's browser, typically used to:
- Track sessions
- Store authentication tokens
- Remember user preferences

**Example structure:**
```

Set-Cookie: session\_id=abc123; Path=/; HttpOnly; Secure

```

## 4. How to Send Cookies

### From Server to Client

The server sends a cookie in the HTTP response using the `Set-Cookie` header:
```http
HTTP/1.1 200 OK
Set-Cookie: session_id=abc123; Path=/; HttpOnly
````

### From Client to Server

The browser automatically includes cookies in subsequent requests:

```http
GET /dashboard HTTP/1.1
Host: example.com
Cookie: session_id=abc123
```

## 5. How to Parse Cookies

### In Python (using `http.cookies`):

```python
from http.cookies import SimpleCookie

raw_cookie = "session_id=abc123; theme=dark"
cookie = SimpleCookie()
cookie.load(raw_cookie)

print(cookie['session_id'].value)  # Output: abc123
```

### In JavaScript:

```javascript
document.cookie  // "session_id=abc123; theme=dark"

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

getCookie('session_id');  // Output: abc123
```
## Summary

Understanding how authentication and cookies work is foundational to web development. Whether using session-based or token-based methods, securely managing and parsing cookies ensures safe and consistent user experiences across web applications.