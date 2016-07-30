import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewUserTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_title_info(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Rideshare', self.browser.title)

    def test_uses_web_design_standards(self):
        self.browser.get('http://localhost:8000')
        try:
            self.browser.find_element_by_css_selector('script[src*=uswds]')
        except:
            self.fail('Web design standards script not on page')

    def test_create_destination_and_see_it(self):
        self.browser.get('http://localhost:8000')
        try:
            link = self.browser.find_element_by_id('create_destination')
        except:
            self.fail('No link to create new destination')

        # She navigates to the Create Destination page
        link.send_keys(Keys.ENTER)

        # but she isn't logged in, so she's asked to

        # now she's logged in
        self.assertIn('Create Destination', self.browser.title)


if __name__ == '__main__':
    # unittest.main(warnings='ignore')
    unittest.main()

# She navigates to the new destination page.

# She is asked to login.

# She enters her destination's information.

# She sees a list of all destinations she's entered.

# She chooses the destination she just entered.

# She is taken to a status page for her destination.

# She uploads a file of attendee data.

# Now her status page reports on potential rideshares.

# She returns to the homepage.
