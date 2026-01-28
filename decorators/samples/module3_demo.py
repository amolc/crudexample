import re

def demo_regex():
    # 1. Basic search
    text = "Contact us at support@example.com or sales@company.org"
    print(f"Text: {text}")
    
    # Extracting emails
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    print(f"Extracted Emails: {emails}")

    # 2. Validation
    def validate_phone(phone):
        # Pattern for (123) 456-7890 or 123-456-7890
        pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
        if re.match(pattern, phone):
            return True
        return False

    phones = ["(123) 456-7890", "123-456-7890", "1234567890", "12-34-56"]
    print("\n--- Phone Validation ---")
    for p in phones:
        status = "Valid" if validate_phone(p) else "Invalid"
        print(f"{p}: {status}")

    # 3. Search and Replace
    price_text = "The price is $100 and the tax is $5"
    print(f"\nOriginal Text: {price_text}")
    # Replace $ with USD
    new_text = re.sub(r'\$', 'USD ', price_text)
    print(f"Updated Text: {new_text}")

    # 4. Splitting strings
    data = "apple,  orange; banana | grape"
    print(f"\nMessy Data: {data}")
    # Split by comma, semicolon, or pipe with optional spaces
    fruits = re.split(r'[,\s;|]+', data)
    print(f"Clean Split: {fruits}")

if __name__ == "__main__":
    demo_regex()
