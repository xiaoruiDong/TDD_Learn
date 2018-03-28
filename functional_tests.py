from selenium import webdriver
# key reader
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

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
        self.browser.get('http://localhost:8000')

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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text == '1: Buy peacock feathers' for row in rows),
        #     "New to-do item did not appear in the table -- its text was:\n%s" % (table.text,)
        # )

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # And at the time, another text box popped out
        inputbox = self.browser.find_element_by_id('id_new_item')

        # We input "Use peacock feathers to make a fly"
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # Webpage refreshed again and showed these 2 To-Do
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # To indicate where are we so far.
        self.fail('Finish the test.')


        # We want to know if the To-Do is saved

        # We will noticed that we are now having our exclusive URL

        # When we visit that url, the list is still there

        # we shut down the webdriver with satisfaction

if __name__ == '__main__':
    unittest.main()


# browser.quit()