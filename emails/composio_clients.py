from django.conf import settings
from composio import Composio
from .models import Email
from datetime import datetime

AUTH_ID = "COMPOSIO_AUTH_ID"


def get_composio_client():
    return Composio(api_key=settings.COMPOSIO_API_KEY)


def fetch_gmail_messages():
    """
    Fetch Gmail messages using Composio
    and store them inside the Email model.
    """

    client = get_composio_client()
    gmail = client.get_action("google_gmail")

    # 1. Fetch list of message IDs
    messages_response = gmail.list_messages(auth_id=AUTH_ID)

    if "messages" not in messages_response:
        return {"error": "No messages found", "raw": messages_response}

    count = 0
    stored_ids = []

    for msg in messages_response["messages"]:
        gmail_id = msg["id"]

        # Skip if already in DB
        if Email.objects.filter(gmail_id=gmail_id).exists():
            continue

        # 2. Fetch full message details
        full_msg = gmail.get_message(auth_id=AUTH_ID, message_id=gmail_id)

        subject = full_msg.get("subject", "(No subject)")
        sender = full_msg.get("sender", "Unknown")
        snippet = full_msg.get("snippet", "")

        # Convert timestamp
        timestamp = full_msg.get("timestamp")
        if timestamp:
            received_at = datetime.fromtimestamp(timestamp / 1000.0)
        else:
            received_at = datetime.now()

        # 3. Save to DB
        email = Email.objects.create(
            gmail_id=gmail_id,
            subject=subject,
            sender=sender,
            snippet=snippet,
            received_at=received_at
        )

        stored_ids.append(gmail_id)
        count += 1

    return {
        "stored": count,
        "stored_ids": stored_ids,
        "total_fetched": len(messages_response["messages"]),
    }
