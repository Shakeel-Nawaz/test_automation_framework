from page_objects.homepage import HomePageObject

def test_landing_page():
    assert 1 == 1
    homepage = HomePageObject(url='https://www.google.com')
    assert homepage.driver.get_title() == "Google", "Landing page title does not match"
    # assert homepage.is_loaded(), "Landing page did not load correctly"
    