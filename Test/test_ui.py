import allure
from selenium import webdriver
from Pages.ExpendedSearchUI import Search

driver = webdriver.Chrome()
search = Search(driver)


@allure.description(
    "Предусловия: "
    '1. Открыть сайт "Кинопоиск", '
    "2. Закрыть pop-up "
    "3. Развернуть окно в полноэкранный режим"
)
@allure.epic("UI. Расширенный поиск фильмов")
@allure.story("UI. Проверка расширенного поиска фильма")
@allure.title("UI. Расширенный поиск по названию фильма")
def test_ui_name(search):
    result_by_name = search.search_by_name()
    print(result_by_name)
    assert result_by_name != 0


@allure.epic("UI. Расширенный поиск фильмов")
@allure.story("UI. Проверка расширенного поиска фильма")
@allure.title("UI. Расширенный поиск по году выхода фильма")
def test_ui_year():
    result_by_year = search.search_by_year()
    print(result_by_year)
    assert result_by_year != 0


@allure.epic("UI. Расширенный поиск фильмов")
@allure.story("UI. Проверка расширенного поиска фильма")
@allure.title("UI. Расширенный поиск по стране")
def test_ui_country():
    result_by_country = search.search_by_country()
    print(result_by_country)
    assert result_by_country != "(0)"


@allure.epic("UI. Расширенный поиск фильмов")
@allure.story("UI. Проверка расширенного поиска фильма")
@allure.title("UI. Расширенный поиск по жанру фильма")
def test_ui_genre():
    result_by_genre = search.search_by_genre()
    print(result_by_genre)
    assert result_by_genre != 0


@allure.epic("UI. Расширенный поиск фильмов")
@allure.story("UI. Проверка расширенного поиска фильма")
@allure.title("UI. Расширенный поиск по прокатчику")
def test_ui_rental_company():
    result_by_rental_company = search.search_by_rental_company()
    print(result_by_rental_company)
    assert result_by_rental_company != 0
