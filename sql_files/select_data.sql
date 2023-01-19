-- 7. найти преподавателя по его имени, фамилии, email:
SELECT Hogwarts_staff.staff_id, first_name, last_name, email, phone_number FROM Hogwarts_staff
FULL JOIN Telephone_number ON Hogwarts_staff.staff_id=Telephone_number.staff_id
WHERE first_name ILIKE 'Albus';
--WHERE last_name ILIKE 'Dumbledore';
--WHERE email = 'albus_dumbledore@gryffindor.hp';
--WHERE phone_number = 89990000001;  -- вернет только 1 номер телефона, а не все!

-- 7. найти преподавателя по его номеру телефона:
-- вариант с вложенным запросом - чтобы получить все номера телефонов сразу:
SELECT Hogwarts_staff.staff_id, first_name, last_name, email, phone_number FROM Hogwarts_staff
FULL JOIN Telephone_number ON Hogwarts_staff.staff_id=Telephone_number.staff_id
WHERE Hogwarts_staff.staff_id = (
    SELECT Hogwarts_staff.staff_id FROM Hogwarts_staff
    JOIN Telephone_number ON Hogwarts_staff.staff_id=Telephone_number.staff_id
    WHERE phone_number = 89990000001
);
