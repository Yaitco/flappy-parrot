#!/bin/bash

# Выводим сообщение
echo "Checking and installing dependencies..."

# Устанавливаем зависимости из requirements.txt
python3 -m pip install -r requirements.txt

# Проверяем, что зависимости установлены успешно
if [ $? -eq 0 ]; then
    echo "Dependencies installed successfully!"
else
    echo "Failed to install dependencies. Exiting."
    exit 1
fi

# Запускаем main.py
echo "Starting the project..."
python3 main.py

# Проверяем, что проект запустился
if [ $? -eq 0 ]; then
    echo "Project finished successfully!"
else
    echo "Project encountered an error."
    exit 1
fi
