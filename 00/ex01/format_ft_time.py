import time
import datetime

def main():
    """Printing exercices"""
    timestamp = time.time()
    # Using fstring to get the correct values
    formatted_timestamp  = f"{timestamp:,.4f} or {timestamp:.2e} in scientific notation"

    current_date = datetime.datetime.now().strftime("%b %d %Y")
    print(f"Seconds since January 1, 1970: {formatted_timestamp}")
    print(current_date)

if __name__ == "__main__":
    main()
