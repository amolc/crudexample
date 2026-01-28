from datetime import datetime, timedelta

def demo_datetime():
    # 1. Current date and time
    now = datetime.now()
    print(f"Current Timestamp: {now}")

    # 2. Formatting (strftime)
    formatted = now.strftime("%A, %d %B %Y - %I:%M %p")
    print(f"Formatted Date: {formatted}")

    # 3. Parsing strings (strptime)
    date_str = "2026-01-28 14:30:00"
    parsed_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    print(f"Parsed Object: {parsed_date}")

    # 4. Date Arithmetic (timedelta)
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    next_week = today + timedelta(weeks=1)

    print("\n--- Date Arithmetic ---")
    print(f"Yesterday: {yesterday}")
    print(f"Today:     {today}")
    print(f"Tomorrow:  {tomorrow}")
    print(f"Next Week: {next_week}")

    # 5. Calculating duration
    start_event = datetime(2026, 1, 1, 0, 0, 0)
    time_passed = now - start_event
    print(f"\nTime passed since New Year 2026: {time_passed.days} days, {time_passed.seconds // 3600} hours")

if __name__ == "__main__":
    demo_datetime()
