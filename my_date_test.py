import unittest
import my_date

class MyDateTest(unittest.TestCase):

    #
    # is_leap_year
    #

    def test_is_leap_year1(self):
        self.assertTrue(my_date.is_leap_year(1984))

    def test_is_leap_year2(self):
        self.assertFalse(my_date.is_leap_year(1985))

    #
    # ordinal_date
    #

    def test_ordinal_date1(self):
        self.assertEqual(1, my_date.ordinal_date(1997, 1, 1))

    def test_ordinal_date2(self):
        self.assertEqual(32, my_date.ordinal_date(1995, 2, 1))

    #
    # days_elapsed  
    #

    def test_days_elapsed1(self):
        self.assertEqual(1, my_date.days_elapsed(1997, 1, 1, 1997, 1, 2))

    def test_days_elapsed2(self):
        self.assertEqual(31, my_date.days_elapsed(1997, 1, 1, 1997, 2, 1))

    def test_days_elapsed3(self):
        self.assertEqual(365, my_date.days_elapsed(1997, 1, 1, 1998, 1, 1))

    # Warning: You need more tests than you think for this function

    #
    # day_of_week
    #

    def test_day_of_week1(self):
        self.assertEqual("Monday", my_date.day_of_week(1753, 1, 1))


    #
    # to_str
    #
    def test_to_str1(self):
        self.assertEqual("Friday, 02 August 2024", my_date.to_str(2024, 8, 2))


import unittest
import my_date


class MyDateTest(unittest.TestCase):

    #
    # is_leap_year
    #

    def test_is_leap_year1(self):
        self.assertTrue(my_date.is_leap_year(1984))

    def test_is_leap_year2(self):
        self.assertFalse(my_date.is_leap_year(1985))

    def test_is_leap_year3(self):
        self.assertTrue(my_date.is_leap_year(800))

    def test_is_leap_year4(self):
        self.assertFalse(my_date.is_leap_year(3001))

    def test_is_leap_year5(self):
        self.assertFalse(my_date.is_leap_year(2023))

    #
    # ordinal_date
    #

    def test_ordinal_date1(self):
        self.assertEqual(74, my_date.ordinal_date(1997, 3, 15))

    def test_ordinal_date2(self):
        self.assertEqual(93, my_date.ordinal_date(1997, 4, 3))

    def test_ordinal_date3(self):
        self.assertEqual(151, my_date.ordinal_date(1997, 5, 31))

    def test_ordinal_date4(self):
        self.assertEqual(181, my_date.ordinal_date(1997, 6, 30))

    def test_ordinal_date5(self):
        self.assertEqual(60, my_date.ordinal_date(1961, 3, 1))

    def test_ordinal_date6(self):
        self.assertEqual(183, my_date.ordinal_date(1997, 7, 2))

    def test_ordinal_date7(self):
        self.assertEqual(233, my_date.ordinal_date(1997, 8, 21))

    def test_ordinal_date8(self):
        self.assertEqual(255, my_date.ordinal_date(1997, 9, 12))

    def test_ordinal_date9(self):
        self.assertEqual(303, my_date.ordinal_date(1997, 10, 30))

    def test_ordinal_date10(self):
        self.assertEqual(310, my_date.ordinal_date(1997, 11, 6))

    def test_ordinal_date11(self):
        self.assertEqual(365, my_date.ordinal_date(1997, 12, 31))

    def test_ordinal_date12(self):
        self.assertEqual(364, my_date.ordinal_date(1997, 12, 30))

    def test_ordinal_date13(self):
        self.assertEqual(91, my_date.ordinal_date(1933, 4, 1))

    def test_ordinal_date14(self):
        self.assertEqual(121, my_date.ordinal_date(1935, 5, 1))

    def test_ordinal_date15(self):
        self.assertEqual(152, my_date.ordinal_date(1998, 6, 1))

    def test_ordinal_date16(self):
        self.assertEqual(182, my_date.ordinal_date(1990, 7, 1))

    def test_ordinal_date17(self):
        self.assertEqual(213, my_date.ordinal_date(1974, 8, 1))

    def test_ordinal_date18(self):
        self.assertEqual(244, my_date.ordinal_date(1975, 9, 1))

    #
    # days_elapsed
    #

    def test_days_elapsed1(self):
        self.assertEqual(31, my_date.days_elapsed(1997, 1, 1, 1997, 2, 1))

    def test_days_elapsed2(self):
        self.assertEqual(365, my_date.days_elapsed(1997, 1, 1, 1998, 1, 1))

    def test_days_elapsed3(self):
        self.assertEqual(365, my_date.days_elapsed(2008, 1, 1, 2008, 12, 31))

    def test_days_elapsed4(self):
        self.assertEqual(730, my_date.days_elapsed(2007, 1, 1, 2008, 12, 31))

    def test_days_elapsed5(self):
        self.assertEqual(0, my_date.days_elapsed(2017, 1, 1, 2017, 1, 1))

    def test_days_elapsed6(self):
        self.assertEqual(32, my_date.days_elapsed(2008, 2, 28, 2008, 3, 31))

    # zk You should have more days_elapsed tests, especially with start-end dates
    # that are farther apart.

    # Warning: You need more tests than you think for this function

    #
    # day_of_week
    #

    def test_day_of_week1(self):
        self.assertEqual("Monday", my_date.day_of_week(1753, 1, 1))

    def test_day_of_week2(self):
        self.assertEqual("Thursday", my_date.day_of_week(2000, 7, 27))

    def test_day_of_week3(self):
        self.assertEqual("Wednesday", my_date.day_of_week(1999, 7, 28))

    def test_day_of_week4(self):
        self.assertEqual("Tuesday", my_date.day_of_week(1998, 4, 21))

    def test_day_of_week5(self):
        self.assertEqual("Sunday", my_date.day_of_week(1999, 5, 9))

    def test_day_of_week6(self):
        self.assertEqual("Friday", my_date.day_of_week(2002, 8, 23))

    def test_day_of_week7(self):
        self.assertEqual("Saturday", my_date.day_of_week(2024, 12, 14))

    #
    # to_str
    #
    def test_to_str1(self):
        self.assertEqual("Monday, 08 January 1753", my_date.to_str(1753, 1, 8))

    def test_to_str2(self):
        self.assertEqual("Tuesday, 13 February 2007", my_date.to_str(2007, 2, 13))

    def test_to_str3(self):
        self.assertEqual("Wednesday, 15 April 1992", my_date.to_str(1992, 4, 15))

    def test_to_str4(self):
        self.assertEqual("Thursday, 25 June 1998", my_date.to_str(1998, 6, 25))

    def test_to_str5(self):
        self.assertEqual("Friday, 02 August 2024", my_date.to_str(2024, 8, 2))

    def test_to_str6(self):
        self.assertEqual("Saturday, 23 August 2003", my_date.to_str(2003, 8, 23))

    def test_to_str7(self):
        self.assertEqual("Sunday, 24 September 2006", my_date.to_str(2006, 9, 24))