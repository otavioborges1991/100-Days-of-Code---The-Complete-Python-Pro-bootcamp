def format_name(first_name, last_name):
    """
    Take a first and last name and format it to return the title case version.
    """
    if not first_name or not last_name:
        return "You didn't provide valid inputs."
    formatted_first = first_name.strip().title()
    formatted_last = last_name.strip().title()
    return f"{formatted_first} {formatted_last}"

# Example usage
formatted_name = format_name("john", "doe")
print(formatted_name)