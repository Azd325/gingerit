import time

import pytest

from gingerit.gingerit import GingerIt


@pytest.fixture(autouse=True)
def _slow_down_tests_for_api():
    # API has a rate limit of 1 request per second
    yield
    time.sleep(1)


@pytest.mark.parametrize(
    ("text", "expected", "corrections"),
    [
        (
            "The smelt of fliwers bring back memories.",
            "The smell of flowers brings back memories.",
            [
                {
                    "start": 21,
                    "definition": None,
                    "correct": "brings",
                    "text": "bring",
                },
                {
                    "start": 13,
                    "definition": "a plant cultivated for its blooms or blossoms",
                    "correct": "flowers",
                    "text": "fliwers",
                },
                {"start": 4, "definition": None, "correct": "smell", "text": "smelt"},
            ],
        ),
        (
            "Edwards will be sck yesterday",
            "Edwards was sick yesterday",
            [
                {
                    "start": 16,
                    "definition": "eject the contents of the stomach through the mouth",
                    "correct": "sick",
                    "text": "sck",
                },
                {"start": 8, "definition": None, "correct": "was", "text": "will be"},
            ],
        ),
        ("Edwards was sick yesterday.", "Edwards was sick yesterday.", []),
    ],
)
def test_gingerit(text, expected, corrections):
    output = GingerIt().parse(text)

    assert output["result"] == expected
    assert output["corrections"] == corrections
