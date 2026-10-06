# selenium-language-tests
# Selenium Language Tests

Автотесты для проверки работы сайта на разных языках интерфейса.

## Файлы

- `conftest.py` — фикстура `browser` и параметр `--language` для pytest.
- `test_items.py` — тест проверки кнопки добавления в корзину.

## Запуск

```bash
pytest --language=es test_items.py
pytest --language=fr test_items.py
