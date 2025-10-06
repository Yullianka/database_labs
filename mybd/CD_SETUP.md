# Continuous Deployment Setup

## 🚀 Автоматичний Deployment з GitHub Actions

### Налаштування GitHub Secrets

1. Перейдіть до вашого GitHub репозиторію
2. Settings → Secrets and variables → Actions
3. Додайте новий секрет:
   - **Name:** `AWS_PRIVATE_KEY`
   - **Value:** Вміст файлу `~/.ssh/database_labs.pem`

### Як працює CD

1. **Автоматичний deployment** - при push в гілку `lab4`
2. **GitHub Actions** виконує:
   - Підключення до AWS EC2
   - Git pull останніх змін
   - Rebuild Docker контейнерів
   - Restart додатку
   - Health check

### Ручний Deployment

```bash
# Локальний deployment через SSH
./ci-deploy.sh

# На сервері (якщо потрібно)
cd /home/ubuntu/database_labs/mybd
sudo ./deploy.sh
```

### Моніторинг

- **Application:** http://54.198.153.234:5000/
- **Swagger UI:** http://54.198.153.234:5000/swagger/
- **Docker logs:** `sudo docker-compose logs -f`

### Workflow файл

`.github/workflows/deploy.yml` - автоматичний deployment при push

### Команди для управління

```bash
# Перегляд статусу
sudo docker-compose ps

# Логи
sudo docker-compose logs -f solar_app

# Restart
sudo docker-compose restart

# Повний rebuild
sudo docker-compose down
sudo docker-compose up -d --build
```

### Troubleshooting

1. **Deployment fails** - перевірте GitHub Secrets
2. **Application не відповідає** - перевірте Docker logs
3. **Database errors** - перевірте RDS підключення

---

✅ **Готово!** Тепер кожен push в `lab4` автоматично деплоїться на сервер!
