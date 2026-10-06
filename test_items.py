<<<<<<< HEAD
import time
from selenium.webdriver.common.by import By


def test_button_add_to_basket_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Пауза 30 секунд для визуальной проверки языка (требование задания)
    time.sleep(30)

    # Ищем кнопку добавления в корзину (уникальный селектор)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

    # Проверяем, что кнопка отображается
    assert button.is_displayed(), \
        "Кнопка добавления в корзину не найдена на странице товара"
=======
import time
from selenium.webdriver.common.by import By


def test_button_add_to_basket_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Пауза 30 секунд для визуальной проверки языка (требование задания)
    time.sleep(30)

    # Ищем кнопку добавления в корзину (уникальный селектор)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

    # Проверяем, что кнопка отображается
    assert button.is_displayed(), \
        "Кнопка добавления в корзину не найдена на странице товара"
>>>>>>> fdd979e849d18d4b493c2c6bf457474bc0219f1e
