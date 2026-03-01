import re
from typing import Any, Dict, Callable


#example text_object: 
# {
#  "hero_alias": "Tony Stark",
#  "secure_contact": "555-0101 (Iron Line)",
#  "raw_text": This is Tony Stark, call me back at 555-0101 (Iron Line)
# }

# This function returns the redacted raw_text, redacting anything that matches either the hero_alias or the secure_contact

def redactPII(text_object: str):
    hero_alias = text_object["hero_alias"]
    secure_contact = text_object["secure_contact"]
    raw_text = text_object["raw_text"]

    redacted_text = raw_text

    if hero_alias in raw_text: 
        redacted_text = redacted_text.replace(hero_alias, "[REDACTED]")

    if secure_contact in raw_text: 
        redacted_text = redacted_text.replace(secure_contact, "[REDACTED]")

    return redacted_text