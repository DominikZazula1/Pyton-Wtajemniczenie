import re

from mod_2.new_movies.actions.cinema import cinema_movies_schedule
from new_movies.actions import user as user_actions


def run_example():
    chubabuba()
    chubabuba2()


def chubabuba():
    matching_examples = ["00-000", "65-197"]
    examples_without_match = ["0-000", "65197", "00a111", "00-14", "aa-bbb"]

    pattern = re.compile(r"\d\d-\d\d\d")

    for example in matching_examples:
        print(pattern.findall(example))

    print(20 * "-")
    for example in examples_without_match:
        print(pattern.findall(example))


def chubabuba2():
    matching_examples = ["AA-000", "AD-1E7"]
    examples_without_match = ["0-0a00", "65197d", "00a111", "00-14", "aa-bbb"]

    pattern = re.compile(r"[A-Z][A-Z]-\w\w\w")

    for example in matching_examples:
        print(pattern.findall(example))

    print(20 * "-")
    for example in examples_without_match:
        print(pattern.findall(example))

if __name__ == "__main__":
    run_example()


