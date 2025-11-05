import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Search:

    @allure.title('UI. Открыть сайт "Кинопоиск"')
    def __init__(self, driver):

        with allure.step("Открыть сайт"):
            self._driver = driver
            self._driver.get("https://www.kinopoisk.ru/")

        with allure.step("Закрыть pop-up"):
            self._wait_popup = WebDriverWait(self._driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[5]/div/div/div/div[1]/div[2]/button[2]")
                )
            )
            self._click_popup = self._driver.find_element(
                By.XPATH, "/html/body/div[5]/div/div/div/div[1]/div[2]/button[2]"
            ).click()

        with allure.step("Развернуть окно в полноэкранный режим"):
            self._driver.maximize_window()
        self._driver.implicitly_wait(20)

    @allure.title("UI. Расширенный поиск по названию фильма")
    def search_by_name(self):

        with allure.step("Кликнуть на кнопку расширенного поиска"):
            self._exp_search_but = self._driver.find_element(
                By.XPATH, "//a[@aria-label='Расширенный поиск']"
            ).click()

        with allure.step('Ввести в поле "Искать фильм:" название фильма'):
            self._find_film = self._driver.find_element(By.ID, "find_film").send_keys(
                "John Wick"
            )

        with allure.step("Кликнуть кнопку поиска"):
            self._wait_but = WebDriverWait(self._driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@class='el_18 submit nice_button']")
                )
            )
            self._click_but = self._driver.find_element(
                By.XPATH, "//input[@class='el_18 submit nice_button']"
            ).click()

        self._search_by_name_result = (
            self._driver.find_element(By.CLASS_NAME, "search_results_topText")
            .text.strip()
            .replace("поиск: John Wick • результаты: ", "")
        )
        print(self._search_by_name_result)
        return int(self._search_by_name_result)

    @allure.title("UI. Расширенный поиск по году выхода фильма")
    def search_by_year(self):

        with allure.step("Кликнуть на кнопку расширенного поиска"):
            self._exp_search_but = self._driver.find_element(
                By.XPATH, "//a[@aria-label='Расширенный поиск']"
            ).click()

        with allure.step('Ввести в поле "+ год:" год выхода фильма'):
            self._find_film_by_year = self._driver.find_element(
                By.ID, "year"
            ).send_keys("1996")

        with allure.step("Кликнуть кнопку поиска"):
            self._wait_but = WebDriverWait(self._driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@class='el_18 submit nice_button']")
                )
            )
            self._click_but = self._driver.find_element(
                By.XPATH, "//input[@class='el_18 submit nice_button']"
            ).click()

        self._search_by_year_result = (
            self._driver.find_element(By.CLASS_NAME, "search_results_topText")
            .text.strip()
            .replace("поиск: • результаты: ", "")
        )
        print(self._search_by_year_result)
        return int(self._search_by_year_result)

    @allure.title("UI. Расширенный поиск по стране")
    def search_by_country(self):

        with allure.step("Кликнуть на кнопку расширенного поиска"):
            self._exp_search_but = self._driver.find_element(
                By.XPATH, "//a[@aria-label='Расширенный поиск']"
            ).click()

        with allure.step('Выбрать страну в выпадающем списке "+ страна:"'):
            self._find_film_by_country = (
                self._driver.find_element(By.ID, "country")
                .find_element(By.XPATH, '//*[@id="country"]/option[43]')
                .click()
            )

        with allure.step("Кликнуть кнопку поиска"):
            self._wait_but = WebDriverWait(self._driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@class='el_18 submit nice_button']")
                )
            )
            self._click_but = self._driver.find_element(
                By.XPATH, "//input[@class='el_18 submit nice_button']"
            ).click()

        self._search_by_country_result = self._driver.find_element(
            By.XPATH,
            '//*[@id="block_left_padtop"]/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/h1/font',
        ).text
        print(self._search_by_country_result)
        return str(self._search_by_country_result)

    @allure.title("UI. Расширенный поиск по жанру фильма")
    def search_by_genre(self):

        with allure.step("Кликнуть на кнопку расширенного поиска"):
            self._exp_search_but = self._driver.find_element(
                By.XPATH, "//a[@aria-label='Расширенный поиск']"
            ).click()

        with allure.step("Выбрать жанр в поле выбора жанра"):
            self._find_film_by_genre = self._driver.find_element(
                By.XPATH, '//*[@id="m_act[genre]"]/option[7]'
            ).click()

        with allure.step("Кликнуть кнопку поиска"):
            self._wait_but = WebDriverWait(self._driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@class='el_18 submit nice_button']")
                )
            )
            self._click_but = self._driver.find_element(
                By.XPATH, "//input[@class='el_18 submit nice_button']"
            ).click()

        self._search_by_genre_result = (
            self._driver.find_element(By.CLASS_NAME, "search_results_topText")
            .text.strip()
            .replace("поиск: • результаты: ", "")
        )
        print(self._search_by_genre_result)
        return int(self._search_by_genre_result)

    @allure.title("UI. Расширенный поиск по прокатчику")
    def search_by_rental_company(self):

        with allure.step("Кликнуть на кнопку расширенного поиска"):
            self._exp_search_but = self._driver.find_element(
                By.XPATH, "//a[@aria-label='Расширенный поиск']"
            ).click()

        with allure.step('Выбрать прокатчика в выпадающем списке "+ прокатчик:"'):
            self._rental_company = self._driver.find_element(
                By.XPATH, '//*[@id="company"]/option[62]'
            ).click()

        with allure.step("Кликнуть кнопку поиска"):
            self._wait_but = WebDriverWait(self._driver, 20).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@class='el_18 submit nice_button']")
                )
            )
            self._click_but = self._driver.find_element(
                By.XPATH, "//input[@class='el_18 submit nice_button']"
            ).click()

        self._search_by_rental_company = (
            self._driver.find_element(By.CLASS_NAME, "search_results_topText")
            .text.strip()
            .replace("поиск: • результаты: ", "")
        )
        print(self._search_by_rental_company)
        return int(self._search_by_rental_company)
