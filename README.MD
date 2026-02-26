# Petstore API Testing — КТ4–7

## Описание
Тесты для API [Petstore](https://petstore.swagger.io/) по сущностям User и Store.  
Для тестирования используются:
- requests, 
- pytest,
- pydantic, 
- allure-pytest.

Для отчетов используются:
- Allure,
- Pytest-Cov.

## Установка зависимостей
```
pip install requests pytest pydantic allure-pytest pytest-cov
npm install -g allure-commandline
```

## Запуск тестов и получение отчета
#### Запуск тестов
``` python -m pytest tests/ --alluredir=allure-results ```

#### Генерация отчета
``` npx allure generate allure-results -o allure-report ```

#### Просмотр отчета
```npx allure open allure-report ```

## Примечания
- В readme используются примеры с npm/npx ибо Allure у меня был установлен именно через npm, в случае если у вас он установлен другим методом - необходимо вызывать Allure иначе.
- Проверка POST/PUT выполняется через GET, так как API не возвращает объект.
- Используется Pydantic через .model_dump().
- Используются Allure-декораторы @allure.feature и @allure.story.

# Полный отчет с описанием этапов доступен в папке !Отчет в форматах pdf и docx.
