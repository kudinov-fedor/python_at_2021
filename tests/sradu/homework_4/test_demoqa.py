from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from tests.sradu.homework_4.utils import (find_element, wait_for_all_elements,
                                          get_menu_item, click_by_action_chains, drag_and_drop_by_action_chains,
                                          scroll_to_element)
from tests.sradu.homework_4.locators import SideMenuLocators, AlertsLocators, DragAndDropLocators
from tests.sradu.homework_4.constants import DEFAULT_TIMEOUT


def test_alert_confirm_box_ok(driver):
    """
    1 - перейти до Alerts, Frame & Windows
    2 - перейти до Alerts
    3 - натиснути `Click me` праворуч від варіанту `On button click, confirm box will appear`
    4 - перевірити, що alert містить дані: Do you confirm action?
    5 - натиснути OK
    6 - перевірити, що варіант `On button click, confirm box will appear` доповнений текстом `You selected OK`
    """

    # 1 - перейти до Alerts, Frame & Windows
    wait_for_all_elements(driver, *SideMenuLocators.LIST_MENU_ITEM)
    menu_item = get_menu_item(driver, SideMenuLocators.LIST_MENU_ITEM, "Alerts, Frame & Windows")
    click_by_action_chains(menu_item)

    # 2 - перейти до Alerts
    menu_sub_item = get_menu_item(driver, SideMenuLocators.LIST_MENU_SUB_ITEM, "Alerts")
    click_by_action_chains(menu_sub_item)

    # 3 - натиснути `Click me` праворуч від варіанту `On button click, confirm box will appear`
    click_button_locator = AlertsLocators.get_click_btn_for_item("On button click, confirm box will appear")
    click_button_element = find_element(driver, *click_button_locator, check=EC.element_to_be_clickable)
    click_by_action_chains(click_button_element)

    # 4 - перевірити, що alert містить дані: Do you confirm action?
    Wait(driver, DEFAULT_TIMEOUT).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "Do you confirm action?", f"Alert text {alert_text} did not match expected text"

    # 5 - натиснути OK
    alert.accept()

    # 6 - перевірити, що варіант `On button click, confirm box will appear` доповнений текстом `You selected OK`
    locator = AlertsLocators.get_alert_result("On button click, confirm box will appear")
    confirm_text_element = find_element(driver, *locator)
    confirm_text = confirm_text_element.text
    assert confirm_text == "You selected Ok", f"Confirm text {confirm_text} did not match expected text"


def test_droppable(driver):
    """
    1 - перейти до Interactions
    2 - перейти до Droppable
    3 - перевірити, що початкова назва більшого блоку, в який пересуватимемо маленький блок, становить `Drop here`
    4 - пересунути блок `Drag me` до блоку `Drop here`
    5 - перевірити, що нова назва більшого блоку, в який пересунуто маленький блок, становить `Dropped!`
    6 - перевірити, що колір більшого блоку синій
    """
    # 1 - перейти до Interactions
    wait_for_all_elements(driver, *SideMenuLocators.LIST_MENU_ITEM)
    menu_item = get_menu_item(driver, SideMenuLocators.LIST_MENU_ITEM, "Interactions")
    click_by_action_chains(menu_item)

    # 2 - перейти до Droppable
    droppable = get_menu_item(driver, SideMenuLocators.LIST_MENU_SUB_ITEM, "Droppable")
    scroll_to_element(driver, droppable)
    click_by_action_chains(droppable)

    # 3 - перевірити, що початкова назва більшого блоку, в який пересуватимемо маленький блок, становить `Drop here`
    droppable_text_locator = DragAndDropLocators.get_locator_for_droppable_text_element("simpleDropContainer")
    droppable_text_element = find_element(driver, *droppable_text_locator)
    droppable_text = droppable_text_element.text
    assert droppable_text == "Drop here", f"Text of droppable block {droppable_text} did not match expected text"

    # 4 - пересунути блок `Drag me` до блоку `Drop here`
    source_locator = DragAndDropLocators.get_locator_for_draggable_element("simpleDropContainer")
    target_locator = DragAndDropLocators.get_locator_for_droppable_element("simpleDropContainer")
    source_element = find_element(driver, *source_locator)
    target_element = find_element(driver, *target_locator)
    drag_and_drop_by_action_chains(source_element, target_element)

    # 5 - перевірити, що нова назва більшого блоку, в який пересунуто маленький блок, становить `Dropped!`
    assert Wait(driver, DEFAULT_TIMEOUT).until(EC.text_to_be_present_in_element(droppable_text_locator, "Dropped!"))

    # 6 - перевірити, що колір більшого блоку синій
    background_color = target_element.value_of_css_property('background-color')
    assert background_color == "rgba(70, 130, 180, 1)"
