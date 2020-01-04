from unittest.mock import call
import pytest
from src.data.preprocessing_helpers import row_to_list, convert_to_int, preprocess

@pytest.fixture
def raw_and_clean_data_file(tmpdir):
    raw_path = tmpdir.join("raw.txt")
    clean_path = tmpdir.join("clean.txt")
    with open(raw_path, "w") as f:
        f.write("1,801\t201,411\n"
                "1,767565,112\n"
                "2,002\t333,209\n"
                "1990\t782,911\n"
                "1,285\t389129\n"
                )
    return raw_path, clean_path


# Define a function convert_to_int_bug_free
def convert_to_int_bug_free(comma_separated_integer_string):
    # Assign to the dict holding the correct return values 
    return_values = {"1,801": 1801,
                     "201,411": 201411,
                     "2,002": 2002,
                     "333,209": 333209,
                     "1990": None,
                     "782,911": 782911,
                     "1,285": 1285,
                     "389129": None}
    # Return the correct result using the dict return_values
    return return_values[comma_separated_integer_string]


class TestRowToList(object):
    def test_on_no_tab_no_missing_value(self):    # (0, 0) boundary value
        # Assign actual to the return value for the argument "123\n"
        actual = row_to_list("123\n")
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_two_tabs_no_missing_value(self):    # (2, 0) boundary value
        actual = row_to_list("123\t4,567\t89\n")
        # Complete the assert statement
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_one_tab_with_missing_value(self):    # (1, 1) boundary value
        actual = row_to_list("\t4,567\n")
        # Format the failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_no_tab_with_missing_value(self):    # (0, 1) case
        # Assign to the actual return value for the argument "\n"
        actual = row_to_list("\n")
        # Write the assert statement with a failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_two_tabs_with_missing_value(self):    # (0, 1) case
        # Assign to the actual return value for the argument "123\t\t89\n"
        actual = row_to_list("123\t\t89\n")
        # Write the assert statement with a failure message
        assert actual is None, "Expected: None, Actual: {0}".format(actual)

    def test_on_normal_argument_1(self):
        actual = row_to_list("123\t4,567\n")
        # Fill in with the expected return value for the argument "123\t4,567\n"
        expected = ["123", "4,567"]
        assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)

    def test_on_normal_argument_2(self):
        actual = row_to_list("1,059\t186,606\n")
        expected = ["1,059", "186,606"]
        # Write the assert statement along with a failure message
        assert actual == expected, "Expected: {0}, Actual: {1}".format(expected, actual)

class TestPreprocess(object):
    # Add the correct argument to use the mocking fixture in this test
    def test_on_raw_data(self, raw_and_clean_data_file, mocker):
        raw_path, clean_path = raw_and_clean_data_file
        # Replace the dependency with the bug-free mock
        convert_to_int_mock = mocker.patch("src.data.preprocessing_helpers.convert_to_int",
                                           side_effect=convert_to_int_bug_free)
        preprocess(raw_path, clean_path)
        # Check if preprocess() called the dependency correctly
        assert convert_to_int_mock.call_args_list == [call("1,801"),
                                                      call("201,411"),
                                                      call("2,002"),
                                                      call("333,209"),
                                                      call("1990"),
                                                      call("782,911"),
                                                      call("1,285"),
                                                      call("389129")]
        with open(clean_path, "r") as f:
            lines = f.readlines()
        first_line = lines[0]
        assert first_line == "1801\t201411\n"
        second_line = lines[1]
        assert second_line == "2002\t333209\n" 