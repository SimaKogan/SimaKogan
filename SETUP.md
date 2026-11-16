# Как запустить

1. Создай на GitHub **публичный** репозиторий с именем, равным твоему username
   (например `mynick/mynick`) — его README показывается на твоём профиле.
2. Локально:
   ```bash
   # профиль уже заполнен в profile.json — правь его при необходимости
   python scripts/build_readme.py           # получишь README.md
   ```
3. Закоммить и запушь:
   ```bash
   git init && git add . && git commit -m "feat: profile README"
   git branch -M main
   git remote add origin git@github.com:<username>/<username>.git
   git push -u origin main
   ```
4. Вкладка **Actions** → *Generate snake animation* → **Run workflow**
   (создаст ветку `output` с анимацией змейки; секреты не нужны).
