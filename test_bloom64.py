"""The false poisitve rate of bloom 64 filter is 0%"""

import pytest
from bloom import BloomFilter64


with open('/Users/user508/PycharmProjects/PythonProject/bad.txt', 'r') as file:
    BAD = [line.rstrip() for line in file]

with open('/Users/user508/PycharmProjects/PythonProject/good.txt', 'r') as file:
    GOOD = [line.rstrip() for line in file]


@pytest.fixture
def filter_64():  # This is run for each test
    yield BloomFilter64() # The test is run here


def test_key_is_not_initially_present(filter_64):
    assert not filter_64.might_contain('badplace.com')


def test_adds_key(filter_64):
    filter_64.add('badplace.com')
    assert filter_64.might_contain('badplace.com')


def test_add_sets_two_bits(filter_64):
    assert filter_64._true_bits() == 0
    filter_64.add('badplace.com')
    assert filter_64._true_bits() == 2
    filter_64.add('awfulplace.com')
    # NOTE: This test will very rarely fail by coincidence
    assert filter_64._true_bits() == 4


def test_add_does_not_add_another_item(filter_64):
    filter_64.add('badplace.com')
    assert not filter_64.might_contain('goodplace.com')


def test_adds_all_entries(filter_64):
    for domain in BAD:
        filter_64.add(domain)
    for domain in BAD:
        assert filter_64.might_contain(domain)


def test_false_positive_rate_is_low(filter_64):
    for domain in BAD:
        filter_64.add(domain)
    print(len(list(filter(filter_64.might_contain, GOOD))) / len(GOOD))
    assert len(list(filter(filter_64.might_contain, GOOD))) < 0.2 * len(GOOD)
