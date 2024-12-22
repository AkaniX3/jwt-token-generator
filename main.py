import secrets

secret_key = secrets.token_urlsafe(64)

print(f"Generated JWT Secret Key: {secret_key}")
