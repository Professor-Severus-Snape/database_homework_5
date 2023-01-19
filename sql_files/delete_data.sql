-- 5. удалить телефон для существующего преподавателя школы Хогвартс:
DELETE FROM Telephone_number
WHERE phone_number = 89999999999;  -- удалить один конкретный телефон

DELETE FROM Telephone_number
WHERE staff_id = 1;  -- удалить все телефоны данного преподавателя


-- 6. удалить существующего преподавателя школы Хогвартс со всеми его данными (например, преподавателя с id=5):
DELETE FROM Telephone_number  -- сначала удаляем все данные из зависимой таблицы
WHERE staff_id = 5;

DELETE FROM Hogwarts_staff  -- затем удаляем все данные из главной таблицы
WHERE staff_id = 5;
