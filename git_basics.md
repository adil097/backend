# Git — это распределённая система управления версиями.

# Начало
git init  # создать репозиторий

# Статус
git status      # посмотреть изменения

# все одним комитом
git add .       # подготовить к сохранению
git commit -m "комментарий"  # сохранить

# Отправка в удаленный репо
git push origin main

# Получение свежего кода
git pull origin main

# комит определенного файла
git add file.py 
git commit -m "описание"

# смотреть историю
git log
git log --oneline 

# изменить комит
git commit --amend -m "новое сообщение"

# git restore file.py      # вернуть к последнему коммиту
git restore .            # всё восстановить

# Откат 
git log                  # копируешь хеш коммита
git reset --hard <хеш>   # откат до этого коммита (удаляет все после)



# мерджим 
git merge feature
# Конфликт:
# Auto-merging main.py
# CONFLICT (content): Merge conflict in main.py
# Automatic merge failed; fix conflicts and then commit the result.

