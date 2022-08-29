import pytest

from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        homepage_nav.close_add()
        actual_links = homepage_nav.get_nal_links_text()
        expected_links = homepage_nav.NAV_LINKS_TEXT
        assert expected_links == actual_links, 'Validating Nav Links text'
