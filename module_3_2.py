def send_email(message, recipient, *, sender="university.help@gmail.com"):  # * перед именованным параметром

    # если recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net" - вывести задан. сообщение
    if not ("@" in recipient and recipient.endswith((".com", ".ru", ".net"))) or not (
            "@" in sender and sender.endswith((".com", ".ru", ".net"))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # проверим совпадает ли адреса отправителя и получателя
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # если отправитель совпадает с university.help@gmail.com, то вывести задан. сообщение
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    # иначе вывести иное сообщение
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")



send_email('Поздравляем! Вы успешно поступили на выбранную программу обучения.', '1912ttanik1912@gmail.cam')
send_email('ОБЩАЯ РАССЫЛКА! Выдача зарплаты за прошлый месяц переносится на новую неделю!', '1912ttanik1912@gmail.com')
send_email('С Новым годом! Пусть этот год будет более благополучным.', '1912ttanik1912@gmail.com', sender='1912ttanik1912@gmail.com')
send_email('Сходить на прием к врачу 28.10.22 в 15:00', 'university.help@gmal.ru', sender='1912ttanik1912@gmail.com')