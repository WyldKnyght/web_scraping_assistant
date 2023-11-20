import secrets

# Generate a random secret key with symbols
secret_key = secrets.token_urlsafe(32)

# Print the secret key
print(secret_key)
