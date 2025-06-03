# Projekt 3 - automatizované testy - Stránka IKEA.cz

def test_homepage_title(page):
    """Test ověření titulku domovské stránky IKEA"""
    page.goto("https://www.ikea.com/cz/cs/")
    page.wait_for_timeout(3000)
    assert "ikea" in page.title().lower()

def test_search_bar_exists(page):
    """Test přítomnosti vyhledávacího pole"""
    page.goto("https://www.ikea.com/cz/cs/")
    page.wait_for_timeout(3000)
    if page.is_visible("button#onetrust-reject-all-handler", timeout=3000):
        page.click("button#onetrust-reject-all-handler")
    search = page.query_selector("#ikea-search-input")
    assert search is not None

def test_search_zidle(page):
    """Test funkce vyhledávání -> zadání 'židle' a zobrazení výsledků"""
    page.goto("https://www.ikea.com/cz/cs/")
    page.wait_for_timeout(3000)
    if page.is_visible("button#onetrust-reject-all-handler", timeout=3000):
        page.click("button#onetrust-reject-all-handler")
    page.fill("#ikea-search-input", "židle")
    page.keyboard.press("Enter")
    # čekaní až se zobrazí produkty
    page.wait_for_selector(".plp-catalog-product-list", timeout=15000)
    product_list = page.locator(".plp-catalog-product-list")
    assert product_list.count() > 0