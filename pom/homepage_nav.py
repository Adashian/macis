from typing import List

from selenium.webdriver.remote.webelement import WebElement

from base.seleniumbase import SeleniumBase
from base.utils import Utils


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#mainNavigationFobs>li'
        self.NAV_LINKS_TEXT = 'Women,Men,Kids & Baby,Home,Shoes,Handbags & Accessories,Jewelry,Sale'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Header Navigation links')

    def close_add(self):
        self.is_present('css', '#closeButton', 'Button for close add').click()
        return self

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_web_elements(nav_links)
        return Utils.join_strings(nav_links_text)

    def get_nav_link_by_text(self, name) -> WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)