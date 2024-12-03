#!/bin/bash

# Определяем директорию проекта
PROJECT_DIR=$(pwd)

# Устанавливаем скрипт my_project в /usr/local/bin
sudo ln -sf "$PROJECT_DIR/run.sh" /usr/local/bin/flappy-parrot

echo "Installation complete! You can now run the project with the command 'flappy-parrot'."
