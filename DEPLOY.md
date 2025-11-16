# Инструкция по настройке деплоя

## Настройка GitHub Secrets

Для работы GitHub Actions необходимо настроить следующие secrets в настройках репозитория:

### Для варианта с Docker Hub (рекомендуется):
1. `DOCKER_USERNAME` - ваш логин на Docker Hub
2. `DOCKER_PASSWORD` - ваш пароль или access token Docker Hub
3. `SERVER_HOST` - IP адрес или домен вашего сервера
4. `SERVER_USER` - имя пользователя для SSH (обычно `root` или `ubuntu`)
5. `SSH_PRIVATE_KEY` - приватный SSH ключ для доступа к серверу
6. `SERVER_PORT` - порт SSH (опционально, по умолчанию 22)

### Для варианта без Docker Hub:
1. `SERVER_HOST` - IP адрес или домен вашего сервера
2. `SERVER_USER` - имя пользователя для SSH
3. `SSH_PRIVATE_KEY` - приватный SSH ключ для доступа к серверу
4. `SERVER_PORT` - порт SSH (опционально)

## Генерация SSH ключа

Если у вас еще нет SSH ключа:

```bash
ssh-keygen -t ed25519 -C "github-actions"
```

Затем скопируйте публичный ключ на сервер:

```bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@your-server
```

Или вручную добавьте содержимое `~/.ssh/id_ed25519.pub` в `~/.ssh/authorized_keys` на сервере.

Приватный ключ (`~/.ssh/id_ed25519`) нужно добавить в GitHub Secrets как `SSH_PRIVATE_KEY`.

## Подготовка сервера

На сервере должен быть установлен Docker:

```bash
# Для Ubuntu/Debian
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
```

## Выбор workflow

В репозитории есть два варианта workflow:

1. **deploy.yml** - сборка образа на сервере (не требует Docker Hub)
2. **deploy-dockerhub.yml** - сборка образа в GitHub Actions и загрузка в Docker Hub, затем pull на сервере (рекомендуется)

Для использования одного из них, переименуйте или удалите ненужный файл.

## Запуск деплоя

Деплой запускается автоматически при push в ветку `main` или вручную через GitHub Actions UI (кнопка "Run workflow").

