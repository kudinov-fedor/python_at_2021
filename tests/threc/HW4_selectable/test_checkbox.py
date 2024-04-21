from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

HOST = 'https://demoqa.com'


def test_checkbox_select_all(driver):
    driver.get(HOST + '/checkbox')
    driver.find_element(By.XPATH, "//*[@id='tree-node']/ol/li/span/label/span[1]").click()

    item_1 = driver.find_element(By.XPATH, "//*[@id='result']/span[2]").text
    assert item_1 in 'home'

    item_2 = driver.find_element(By.XPATH, "//*[@id='result']/span[3]").text
    assert item_2 in 'desktop'

    item_3 = driver.find_element(By.XPATH, "//*[@id='result']/span[4]").text
    assert item_3 in 'notes'

    item_4 = driver.find_element(By.XPATH, "//*[@id='result']/span[5]").text
    assert item_4 in 'commands'

    item_5 = driver.find_element(By.XPATH, "//*[@id='result']/span[6]").text
    assert item_5 in 'documents'

    item_6 = driver.find_element(By.XPATH, "//*[@id='result']/span[7]").text
    assert item_6 in 'workspace'

    item_7 = driver.find_element(By.XPATH, "//*[@id='result']/span[8]").text
    assert item_7 in 'react'

    item_8 = driver.find_element(By.XPATH, "//*[@id='result']/span[9]").text
    assert item_8 in 'angular'

    item_9 = driver.find_element(By.XPATH, "//*[@id='result']/span[10]").text
    assert item_9 in 'veu'

    item_10 = driver.find_element(By.XPATH, "//*[@id='result']/span[11]").text
    assert item_10 in 'office'

    item_11 = driver.find_element(By.XPATH, "//*[@id='result']/span[12]").text
    assert item_11 in 'public'

    item_12 = driver.find_element(By.XPATH, "//*[@id='result']/span[13]").text
    assert item_12 in 'private'

    item_13 = driver.find_element(By.XPATH, "//*[@id='result']/span[14]").text
    assert item_13 in 'classified'

    item_14 = driver.find_element(By.XPATH, "//*[@id='result']/span[15]").text
    assert item_14 in 'general'

    item_15 = driver.find_element(By.XPATH, "//*[@id='result']/span[16]").text
    assert item_15 in 'downloads'

    item_16 = driver.find_element(By.XPATH, "//*[@id='result']/span[17]").text
    assert item_16 in 'wordFile'

    item_17 = driver.find_element(By.XPATH, "//*[@id='result']/span[18]").text
    assert item_17 in 'excelFile'

    driver.close()


def test_checkbox_select_several(driver):
    driver.get(HOST + '/checkbox')
    driver.find_element(By.CSS_SELECTOR, ".rct-option-expand-all").click()

    driver.find_element(By.XPATH, "//*[@id='tree-node']/ol/li/ol/li[1]/span/label/span[3]").click()

    item_1 = driver.find_element(By.XPATH, "//*[@id='result']/span[2]").text
    assert item_1 in 'desktop'

    item_2 = driver.find_element(By.XPATH, "//*[@id='result']/span[3]").text
    assert item_2 in 'notes'

    item_3 = driver.find_element(By.XPATH, "//*[@id='result']/span[4]").text
    assert item_3 in 'commands'

    driver.close()


def test_expand(driver):
    driver.get(HOST + '/checkbox')
    driver.find_element(By.XPATH, "//*[@id='tree-node']/div/button[1]").click()

    driver.find_element(By.XPATH, "//*[@id='tree-node']/ol/li/span/label/span[1]").click()

    scroll_origin = ScrollOrigin.from_viewport(10, 10)

    ActionChains(driver) \
        .scroll_from_origin(scroll_origin, 0, 200) \
        .perform()

    item_1 = driver.find_element(By.XPATH, "//*[@id='result']/span[2]").text
    assert item_1 in 'home'

    item_2 = driver.find_element(By.XPATH, "//*[@id='result']/span[3]").text
    assert item_2 in 'desktop'

    item_3 = driver.find_element(By.XPATH, "//*[@id='result']/span[4]").text
    assert item_3 in 'notes'

    item_4 = driver.find_element(By.XPATH, "//*[@id='result']/span[5]").text
    assert item_4 in 'commands'

    item_5 = driver.find_element(By.XPATH, "//*[@id='result']/span[6]").text
    assert item_5 in 'documents'

    item_6 = driver.find_element(By.XPATH, "//*[@id='result']/span[7]").text
    assert item_6 in 'workspace'

    item_7 = driver.find_element(By.XPATH, "//*[@id='result']/span[8]").text
    assert item_7 in 'react'

    item_8 = driver.find_element(By.XPATH, "//*[@id='result']/span[9]").text
    assert item_8 in 'angular'

    item_9 = driver.find_element(By.XPATH, "//*[@id='result']/span[10]").text
    assert item_9 in 'veu'

    item_10 = driver.find_element(By.XPATH, "//*[@id='result']/span[11]").text
    assert item_10 in 'office'

    item_11 = driver.find_element(By.XPATH, "//*[@id='result']/span[12]").text
    assert item_11 in 'public'

    item_12 = driver.find_element(By.XPATH, "//*[@id='result']/span[13]").text
    assert item_12 in 'private'

    item_13 = driver.find_element(By.XPATH, "//*[@id='result']/span[14]").text
    assert item_13 in 'classified'

    item_14 = driver.find_element(By.XPATH, "//*[@id='result']/span[15]").text
    assert item_14 in 'general'

    item_15 = driver.find_element(By.XPATH, "//*[@id='result']/span[16]").text
    assert item_15 in 'downloads'

    item_16 = driver.find_element(By.XPATH, "//*[@id='result']/span[17]").text
    assert item_16 in 'wordFile'

    item_17 = driver.find_element(By.XPATH, "//*[@id='result']/span[18]").text
    assert item_17 in 'excelFile'

    driver.close()
