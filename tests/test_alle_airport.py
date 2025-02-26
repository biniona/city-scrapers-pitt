from datetime import datetime
from os.path import dirname, join

import pytest
from city_scrapers_core.constants import NOT_CLASSIFIED
from city_scrapers_core.utils import file_response
from freezegun import freeze_time

from city_scrapers.spiders.alle_airport import AlleAirportSpider

test_response = file_response(
    join(dirname(__file__), "files", "alle_airport.html"),
    url="https://www.flypittsburgh.com/about-us/leadership",
)
spider = AlleAirportSpider()

freezer = freeze_time("2019-11-04")
freezer.start()

parsed_items = [item for item in spider.parse(test_response)]

freezer.stop()

# def test_tests():
#     print("Please write some tests for this spider or at least disable this one.")
#     assert False
"""
Uncomment below
"""


def test_title():
    assert parsed_items[0]["title"] == "Allegheny County Airport Authority Board Meeting"


def test_description():
    assert parsed_items[0]["description"] == ""


def test_start():
    assert parsed_items[0]["start"] == datetime(2019, 1, 18, 11, 30, 0)


def test_end():
    assert parsed_items[0]["end"] == None


def test_time_notes():
    assert parsed_items[0]["time_notes"] == ""


# def test_id():
#     assert parsed_items[0]["id"] == "EXPECTED ID"

# def test_status():
#     assert parsed_items[0]["status"] == "EXPECTED STATUS"


def test_location():
    assert parsed_items[0]["location"] == {
        "name": "Pittsburgh International Airport",
        "address": "Conference Room A, 4th Flr Mezzanine,"\
                   " Landside Terminal, Pittsburgh International Airport"
    }


def test_source():
    assert parsed_items[0]["source"] == "https://www.flypittsburgh.com/about-us/leadership"


def test_links():
    assert parsed_items[0]["links"] == [{
        "href": "https://www.flypittsburgh.com/about-us/leadership",
        "title": "Leadership - Pittsburgh International Airport"
    }]


def test_classification():
    assert parsed_items[0]["classification"] == NOT_CLASSIFIED


# @pytest.mark.parametrize("item", parsed_items)
# def test_all_day(item):
#     assert item["all_day"] is False
