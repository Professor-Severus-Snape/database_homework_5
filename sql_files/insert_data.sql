-- 2. добавление нового преподавателя школы Хогвартс:
INSERT INTO Hogwarts_staff
    (staff_id, first_name, last_name, email)
VALUES
	(1, 'Albus', 'Dumbledore', 'albus_dumbledore@gryffindor.hp'),
	(2, 'Severus', 'Snape', 'severus_snape@slytherin.hp'),
	(3, 'Minerva', 'McGonagall', 'minerva_mcgonagall@gryffindor.hp'),
	(4, 'Filius', 'Flitwick', 'filius_flitwick@ravenclaw.hp'),
	(5, 'Pomona', 'Sprout', 'pomona_sprout@hufflepuff.hp'),
	(6, 'Remus', 'Lupin', 'remus_lupin@gryffindor.hp'),
	(7, 'Rubeus', 'Hagrid', 'rubeus_hagrid@gryffindor.hp'),
	(8, 'Sybill', 'Trelawney', 'sybill_trelawney@ravenclaw.hp'),
	(9, 'Gilderoy', 'Lockhart', 'gilderoy_lockhart@ravenclaw.hp'),
	(10, 'Horace', 'Slughorn', 'horace_slughorn@slytherin.hp'),
	(11, 'Alastor', 'Moody', 'alastor_moody@gryffindor.hp');


-- 3. добавление телефона для существующего преподавателя школы Хогвартс:
INSERT INTO Telephone_number
    (staff_id, phone_number)
VALUES
	(1, 89999999999),
	(1, 89990000001),
	(2, 89990000002),
	(3, 89990000003),
	(4, 89990000004),
	(5, 89990000005),
	(6, 89990000006),
	(7, 89990000007),
	(8, 89990000008),
	(9, 89990000009),
	(10, 89990000010),
    (11, 89990000011);
