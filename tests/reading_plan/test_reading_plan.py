from unittest.mock import patch
from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501


list_mock = [
    {
        "titile": "news mock 01",
        "reading_time": "10",
    },
    {
        "titile": "news mock 02",
        "reading_time": "5",
    },
    {
        "titile": "news mock 03",
        "reading_time": "8",
    },
    {
        "titile": "news mock 04",
        "reading_time": "20",
    },
]

reading_plan_mock = {
    "readable": [
        {
            "unfilled_time": 3,
            "chosen_news": [
                (
                    "news mock 03",
                    5,
                ),
            ],
        },
        {
            "unfilled_time": 0,
            "chosen_news": [
                (
                    "news mock 03",
                    8,
                )
            ],
        },
    ],
    "unreadable": [
        ("news mock 01", 10),
        ("news mock 04", 20),
    ],
}


def test_reading_plan_group_news():
    with patch("tech_news.database.find_news") as mock_function:
        mock_function.return_value = list_mock

        reading_plan = ReadingPlanService.group_news_for_available_time(8)
        assert reading_plan == reading_plan_mock
