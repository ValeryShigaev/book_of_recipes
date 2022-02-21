# book_of_recipes
Веб-сайт "Книга рецептов"

## Настройка проекта и запуск контейнеров
- По необходимости отредактируйте .env.dev, но лучше не стоит
- В корне репозитория выполните команду:
  > docker-compose up --build
- Миграции создадутся и применятся автоматически, также автоматически загрузятся фикстуры
- Для остановки контейнеров:
  > docker-compose stop

## Работа с проектом
- Проект доступен по ссылке **127.0.0.1:8000**
- Создавать рецепты может только аутентифицированный пользователь
- Если нет желания проходить регистрацию, в проекте есть пользователь **test** **admin732**
- Рецепты создаются в админ-панели, обычный пользователь имеет доступ только к своим рецептам
- В публичной части сайта есть фильтры по названию и ингредиентам
