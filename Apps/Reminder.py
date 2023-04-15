import datetime
import time
from plyer import notification

# Установить дату и время напоминания
reminder_datetime = datetime.datetime(2023, 4, 11, 18, 11, 0)

# Функция, которая создает уведомление
def show_reminder():
    notification.notify(
        title="Напоминание",
        message="Пора сделать перерыв!",
        timeout=None,
        app_name="My Reminder",
        app_icon="path/to/icon.ico"
    )

# Функция, которая вызывается при клике на уведомление
def on_reminder_click():
    print("Уведомление было нажато!")

# Бесконечный цикл, который проверяет, наступило ли время напоминания
while True:
    # Получить текущую дату и время
    now = datetime.datetime.now()

    # Если наступило время напоминания, показать уведомление
    if now >= reminder_datetime:
        show_reminder()
        notification.on_click = on_reminder_click
        break

    # Подождать 1 минуту перед следующей проверкой времени
    time.sleep(60)
