# ⚖️ MSPro Legal Agent — OpenAPI Schema

## 📘 Назначение
Официальная схема юридического агента **MSPro Legal Agent**.  
Работает через Supabase (`https://lmqhpvqhardpluneonul.supabase.co`),  
bucket `legal/inbox`, с автоматической индексацией документов через pgvector.

---

## 🚀 Подключение в ChatGPT Actions
1. Откройте **ChatGPT → Настройки → Actions → Create new action**.  
2. Выберите **Import from URL**.  
3. Вставьте ссылку:
   ```
   https://raw.githubusercontent.com/vladimirspecalp-hub/mspro_legal_law/main/openapi.json
   ```
4. ChatGPT автоматически создаст интеграцию MSPro Legal Agent.

---

## 🔄 Как обновлять схему агента
1. Вносите изменения в файл `openapi.json` в репозитории.  
2. Делайте коммит с пометкой, например:
   ```
   git commit -m "v1.4: добавлена функция get_case_status"
   ```
3. В ChatGPT → Actions → Import from URL снова вставьте ссылку (она останется той же).  
4. ChatGPT подхватит новую версию схемы автоматически.

---

## 📂 Структура API
- **storage_upload_legal** — загрузка файлов в Supabase Storage.
- **stage_file_ref** — регистрация загруженного файла в буфере.
- **commit_session** — фиксация документов и генерация public URL.
- **find_documents** — поиск документов по делу.
- **public_link_by_path** — генерация ссылки для скачивания.
- **embed_document** — автоиндексация документа (pgvector).

---

## 🛠️ Служебные скрипты
- `scripts/check_openapi_action_endpoints.py` — проверяет, что все пути из
  `openapi_action.json` реально отдают HTTP 200 по адресу GitHub Raw. Запустите
  его из корня репозитория:

  ```bash
  ./scripts/check_openapi_action_endpoints.py
  ```

---

© MSPRO Legal Division
