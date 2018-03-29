from django.test import LiveServerTestCase

from selenium import webdriver
# key reader
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest
import time

#class NewVisitorTest(unittest.TestCase):


class NewVistorTest(LiveServerTestCase):

    # used before test
    def setUp(self):
        self.browser = webdriver.Firefox()

        # wait for some time
        self.browser.implicitly_wait(3)
    # used after test, even if error occurs, tearDown also be executed
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    # start with test is test method:
    def test_can_start_a_list_and_retrieve_it_later(self):
        # we have a new website launched online and we will visit it right now
        # self.browser.get('http://localhost:8000')

        # using live server url
        self.browser.get(self.live_server_url)

        # we will notice that there is To-Do in both of the title and the head
        # assert 'To-Do' in browser.title, "Broweser title was " + browser.title
        self.assertIn('To-Do', self.browser.title)
        # we also have assertEqual, assertTrue, assertFalse

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Then we will make a to-do list
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item',
        )

        # we first type "Buy peacock feathers" in the text box
        inputbox.send_keys('Buy peacock feathers')

        # after pressing enter, the webpage is refreshed with '1: Buy peacock feathers'
        inputbox.send_keys(Keys.ENTER)

        # Assertion used to know if the key words are contained
        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     "New to-do item did not appear in the table -- its text was:\n%s" % (table.text,)
        # )

        # some magic lines that can avoid stale problem
        WebDriverWait(self.browser, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.ID, 'id_list_table'), 'Buy peacock feathers'
        ))

        # create the owner exclusive url
        edith_list_url = self.browser.current_url
        # regex used to testify whether strings and canonical expression is matched
        self.assertRegexpMatches(edith_list_url, '/lists/.+')

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # And at the time, another text box popped out
        inputbox = self.browser.find_element_by_id('id_new_item')

        # We input "Use peacock feathers to make a fly"
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # Webpage refreshed again and showed these 2 To-Do
        WebDriverWait(self.browser, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.ID, 'id_list_table'), 'Use peacock feathers to make a fly'
        ))

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        WebDriverWait(self.browser, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.ID, 'id_list_table'), 'Buy peacock feathers'
        ))

        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        ## Francis also visit the website
        ## we use a new webdriver and should make sure that edith info is not leaked
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis see the homepage and cannot see Edith's info
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text

        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis also add a new item and a new list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        WebDriverWait(self.browser, 10).until(expected_conditions.text_to_be_present_in_element(
             (By.ID, 'id_list_table'), 'Buy milk'
        ))

        self.check_for_row_in_list_table('1: Buy milk')

        # Francis also get his exclusive url
        francis_list_url = self.browser.current_url
        # assertRegex is in Python3, we should use assertRegexpMatches()
        self.assertRegexpMatches(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Within this page, there is still no edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # We want to know if the To-Do is saved

        # To indicate where are we so far.
        self.fail('Finish the test.')

        # We will noticed that we are now having our exclusive URL

        # When we visit that url, the list is still there

        # we shut down the webdriver with satisfaction

# if __name__ == '__main__':
#    unittest.main()


# browser.quit()