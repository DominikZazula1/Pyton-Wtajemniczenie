import re

from mod_2.new_movies.actions.cinema import cinema_movies_schedule
from new_movies.actions import user as user_actions


def run_example():
    chubabuba3()


def find_all_emails(text):
    email_pattern = re.compile(r"(\w+)@(\w+)((?:\.\w+)+)")
    email_matches = email_pattern.findall(text)
    print(20 * "-")
    if email_matches is None:
        print("text doesn't contains email")
        return
    for email_match in email_matches:
        print_email_details(email_match)


def find_iter_emails(text):
    email_pattern = re.compile(r"(\w+)@(\w+)((?:\.\w+)+)")
    email_matches = email_pattern.finditer(text)
    print(20 * "-")
    if email_matches is None:
        print("text doesn't contains email")
        return
    for email_match in email_matches:
        print_email_details(email_match)


def print_email_details(email):
    print(f"{email[0]} to positions: {email.start()} - {email.end()}")
    print(20 * "-")
    print(f"name:\t\t{email[1]}")
    print(f"domain:\t\t{email[2]}")
    print(f"extension:\t{email[3]}")
    print(20 * "-")


def chubabuba2():
    matching_examples = ["AA-000", "AD-1E7", "BB123"]
    examples_without_match = ["0-0a00", "65197d", "00a111", "00-14", "aa-bbb"]

    pattern = re.compile(r"[A-Z]{2}-?\w{3}")

    for example in matching_examples:
        print(pattern.findall(example))

    print(20 * "-")
    for example in examples_without_match:
        print(pattern.findall(example))
    print(20 * "-")


def chubabuba3():
    user_email = input("Enter your email: ")
    email_pattern = re.compile(r"(\w+)@(\w+)((?:\.(?:pl|com)))", flags=re.IGNORECASE)
    email_match = email_pattern.fullmatch(user_email)
    print(20 * "-")
    if email_match is None:
        print("this is not email")
        return
    print(f"name:\t\t{email_match[1]}")
    print(f"domain:\t\t{email_match[2]}")
    print(f"extension:\t{email_match[3]}")


def chubabuba4():
    matching_examples = ["https://www.dominikiteria.pl", "www.alamakotadomeroty.com"]
    examples_without_match = ["htts://www.dominikiteria.pl", "https//www.dominikiteria.pl", "https://dominikiteria", "http:/alamakota@domeroty.com", "aa-bbasdddb"]

    pattern = re.compile(r"^(?:(https|http)://)?www\.(\w+)\.\w+")
    for example in matching_examples:
        print(pattern.findall(example))

    print(20 * "-")
    for example in examples_without_match:
        print(pattern.findall(example))
    print(20 * "-")


if __name__ == "__main__":
    run_example()


