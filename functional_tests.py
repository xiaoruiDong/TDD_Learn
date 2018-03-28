from selenium import webdriver
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

    # start with test is test method:
    def test_can_start_a_list_and_retrieve_it_later(self):
        # we have a new website launched online and we will visit it right now
        self.browser.get('http://localhost:8000')

        # we will notice that there is To-Do in both of the title and the head
        # assert 'To-Do' in browser.title, "Broweser title was " + browser.title
        self.assertIn('To-Do',self.browser.title)
        # we also have assertEqual, assertTrue, assertFalse
        self.fail('Finish the test.')

        # Then we will make a to-do list

        # we first type "Buy peacock feathers" in the text box

        # after pressing enter, the webpage is refreshed with '1: Buy peacock feathers'

        # And at the time, another text box popped out

        # We input "Use peacock feathers to make a fly"

        # Webpage refreshed again and showed these 2 To-Do

        # We want to know if the To-Do is saved

        # We will noticed that we are now having our exclusive URL

        # When we visit that url, the list is still there

        # we shut down the webdriver with satisfaction

if __name__ == '__main__':
    unittest.main()


# browser.quit()