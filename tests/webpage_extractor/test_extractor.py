from unittest import mock

import webpage_extractor.extractor as ext


def test_last_saved_report_id():
    with mock.patch("os.listdir") as listdir_mock:
        # It found two valid files and one invalid file extension (json)
        listdir_mock.return_value = ["100.html", "101.html", "something_else.json"]
        response = ext.last_saved_report_id("folder_path")
        assert response == 101

        # It found only invalid file extensions (different than html)
        listdir_mock.return_value = ["README.md", "something_else.json"]
        response = ext.last_saved_report_id("folder_path")
        assert response == 200_000


def test_get_longest_run():
    with mock.patch("os.listdir") as listdir_mock:
        # Longest run is 2 (100 -> 101, 101 -> 102)
        files_name = [100, 101, 102, 105]
        files_name = [f"{each}.txt" for each in files_name]
        listdir_mock.return_value = files_name
        assert ext.get_longest_run("folder_path") == (2, 102)

        # Longest run is 0
        files_name = [100, 105, 108, 110]
        files_name = [f"{each}.txt" for each in files_name]
        listdir_mock.return_value = files_name
        assert ext.get_longest_run("folder_path") == (0, None)
