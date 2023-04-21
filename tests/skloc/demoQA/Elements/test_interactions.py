import pytest
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True, scope="function")
def test_setup(driver):
    driver.get("https://demoqa.com/droppable")


def test_simple(driver):
    draggable_box = driver.find_element(By.CSS_SELECTOR, "#draggable")
    droppable_box = driver.find_element(By.CSS_SELECTOR, "#droppable")

    AC(driver).drag_and_drop(draggable_box, droppable_box).perform()

    droppable_box_text = driver.find_element(By.CSS_SELECTOR, "#droppable p").text

    assert droppable_box_text == "Dropped!"


def test_revert_draggable(driver):
    revert_draggable_tab = driver.find_element(By.CSS_SELECTOR, "#droppableExample-tab-revertable")
    revert_draggable_tab.click()

    droppable_box = driver.find_element(By.CSS_SELECTOR, "#droppableExample-tabpane-revertable #droppable")
    revertible = driver.find_element(By.CSS_SELECTOR, "#droppableExample-tabpane-revertable #revertable")
    revertible_x_position = revertible.location["x"]
    not_revertible = driver.find_element(By.CSS_SELECTOR, "#droppableExample-tabpane-revertable #notRevertable")
    not_revertible_x_position = not_revertible.location["x"]

    AC(driver) \
        .drag_and_drop(revertible, droppable_box) \
        .drag_and_drop(not_revertible, droppable_box)\
        .perform()

    tab_el = driver.find_element(By.CSS_SELECTOR, "#droppableExample-tabpane-revertable")
    updated_location_revertible = tab_el.find_element(By.CSS_SELECTOR, "#revertable").location["x"]
    updated_location_not_revertible = tab_el.find_element(By.CSS_SELECTOR, "#notRevertable").location["x"]

    assert not_revertible_x_position != updated_location_not_revertible
    assert revertible_x_position == updated_location_revertible
