from main import BooksCollector
import pytest
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_book_twice(self):
        collector = BooksCollector()
        book_name = 'Detective story'
        collector.add_new_book(name=book_name)
        collector.add_new_book(name=book_name)

        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_for_not_added_book(self):
        collector = BooksCollector()
        not_added_book_name = 'No Book'
        collector.set_book_rating(name=not_added_book_name, rating=1)

        assert collector.get_book_rating(name=not_added_book_name) is None



@pytest.mark.parametrize(
    'name,rating',
    [
        ['Lowest Rating', 1],
        ['Mid Rating', 5],
        ['Highest Rating', 10]
        ]
)
def test_set_book_rating(name, rating):
    collector = BooksCollector()
    collector.add_new_book(name)
    collector.set_book_rating(name, rating)

    assert collector.get_book_rating(name) == rating


def test_add_book_in_favorites():
    collector = BooksCollector()
    new_book_name = 'Favorite Book'
    collector.add_new_book(name=new_book_name)
    collector.add_book_in_favorites(name=new_book_name)

    assert len(collector.get_list_of_favorites_books()) == 1






