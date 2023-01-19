-- для существующего преподавателя школы Хогвартс (например, преподавателя с id=11)
-- 4. изменить номер телефона:
UPDATE Telephone_number SET phone_number = 89990000111
WHERE staff_id = 11;

-- 4. изменить имя преподавателя
UPDATE Hogwarts_staff SET first_name = 'Alastor Mad_Eye'
WHERE staff_id = 11;

-- 4. изменить фамилию преподавателя
UPDATE Hogwarts_staff SET last_name = 'Mad_Eye Moody'
WHERE staff_id = 11;

-- 4. изменить электронный адрес преподавателя
UPDATE Hogwarts_staff SET email = 'alastor_mad_eye_moody@gryffindor.hp'
WHERE staff_id = 11;
