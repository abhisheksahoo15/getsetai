import os
import json
from google.oauth2 import service_account

GOOGLE_CREDENTIALS_JSON = os.getenv("GOOGLE_CREDENTIALS_JSON")

if not GOOGLE_CREDENTIALS_JSON:
    raise ValueError("❌ GOOGLE_CREDENTIALS_JSON env var is not set.")

try:
    GOOGLE_CREDENTIALS = service_account.Credentials.from_service_account_info(
        json.loads(GOOGLE_CREDENTIALS_JSON)
    )
except Exception as e:
    raise RuntimeError(f"❌ Failed to load Google service account: {e}")
