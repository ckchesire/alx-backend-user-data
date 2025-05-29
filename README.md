# ALX Backend - User Data

This repository contains projects focused on handling user data responsibly, securely, and effectively in backend systems.

## Project Structure

### `0x00-personal_data`
This project focuses on:
- Understanding what **PII (Personally Identifiable Information)** is.
- Implementing **logging** while ensuring sensitive data is **masked or redacted**.
- Safely handling user information to comply with best practices and privacy standards.

### `0x01-Basic_authentication`
This project covers:
- The basics of **HTTP authentication**, particularly **Basic Authentication**.
- How to encode credentials using **Base64**.
- Setting and sending the `Authorization` header in HTTP requests.
- Implementing a basic authentication class for verifying users.

### `0x02-Session_authentication`

This section focuses on **Session-Based Authentication**, where the server maintains user login state across multiple requests. This project covers:
- **Session Authentication**:
  - Users authenticate once, and the server maintains a session ID to identify them on subsequent requests.
- **Session Management**:
  - Generating and storing session IDs server-side (e.g., in memory or a database).
- **Cookies**:
  - How session IDs are stored and transmitted between client and server using cookies.
  - Sending cookies from server to client via the `Set-Cookie` header.
  - Client sending cookies back using the `Cookie` header.
- **Parsing Cookies**:
  - Extracting session IDs and other key-value pairs from cookies
- **Implementing a SessionAuth Class**:
  - Creating a class that generates and validates sessions to manage authenticated user access.

## Key Concepts
- PII (Personally Identifiable Information)
- Logging and data privacy
- Base64 encoding
- Basic Auth mechanism in HTTP
- Authorization headers
- Session-based authentication
