def convert_to_24_hour(hour, minute, period):
    # Check if it's 'am'
    if period == 'am':
        # If hour is 12 am, convert it to 0
        if hour == 12:
            hour = 0
    else:
        # If it's 'pm' and not 12 pm, add 12 to the hour
        if hour != 12:
            hour += 12
    # Return the time in 24-hour format with zero-padding
    return f"{hour:02d}{minute:02d}"

hour = 4
minute = 30
period = 'pm'

# Convert 12-hour time to 24-hour time
result = convert_to_24_hour(hour, minute, period)
print(f"The 24-hour format is: {result}")