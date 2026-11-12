# Тренажёр английского произношения

Учебный проект: находит ошибки в произношении английских звуков и подсказывает, что прозвучало вместо ожидаемого звука.

## Требования

- Git
- Python 3.12. При установке через uv он скачается автоматически.
- Видеокарта NVIDIA — нужна только для обучения моделей. Без неё всё работает на процессоре, просто медленнее.

## Установка через uv

1. Установите [uv](https://docs.astral.sh/uv/):

   ```powershell
   # Windows (PowerShell)
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

   ```bash
   # Linux / macOS
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
   После установки перезапустите терминал.


2. Склонируйте репозиторий и установите зависимости:

   ```bash
   git clone https://github.com/FandH0/CAPT-web.git
   cd CAPT-web
   uv sync
   ```
   `uv sync` сам скачает нужную версию Python, создаст окружение `.venv` и поставит точные версии пакетов из `uv.lock`.


3. Проверьте установку:

   ```bash
   uv run python scripts/check_env.py
   ```
   

## Что должна показать проверка
 

- На компьютере с видеокартой NVIDIA: `видеокарта доступна: True` и название GPU.
- На компьютере без видеокарты NVIDIA: `видеокарта доступна: False`.


## Частые проблемы

| Проблема | Решение |
|---|---|
| Команда `uv` не найдена | Перезапустите терминал. Если не помогло, выполните `uv tool update-shell`, запустив uv по полному пути (`%USERPROFILE%\.local\bin\uv.exe` на Windows, `~/.local/bin/uv` на Linux/macOS) |
| Видеокарта NVIDIA есть, но проверка пишет `False` | Выполните `nvidia-smi`: значение `CUDA Version` должно быть не ниже варианта CUDA в `pyproject.toml`. Если ниже, обновите драйвер NVIDIA |
| PyCharm не видит пакеты | Settings → Project → Python Interpreter → выберите `.venv` в корне проекта |