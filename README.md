Логин и пароль: admin / 123456
dimac@Dimac--MacBook-Pro ~/Projects/Polyposis                                                     

# Для обновления зависимостей необходимо (ВНЕ КОНТЕЙНЕРА)
1. Локально создать вертуальное окружение с версией python, которая указана в pyproject.toml
```bash
python3.13 -m venv .venv
```

2. Активировать виртуальное окружение
```bash
source .venv/bin/activate
```

4. Установить poetry в созданный .venv той же версии что и в ci/Dockerfile.dev
```bash
pip install "poetry==1.8.2"
```

5. Изменить/добавить библиотеки в pyproject.toml

6. Обновить poetry.lock файл
```bash
poetry lock
```

7. Установить обновлённые зависимости
```bash
poetry install
```

# Команда для подключения к контейнеру
```bash
docker exec -it polyposis-app-1 bash  
```

После подключения по команде выше необходимо создать суперпользователя и произвести дальнейшую настройку.