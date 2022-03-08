-- check crime_scene_reports table for getting some information
SELECT description FROM crime_scene_reports WHERE(year = 2020 AND month = 7 AND day = 28 AND street = "Chamberlin Street");

-- all interviews that might related to the theft including 3 witnessess that we are looking for
SELECT transcript FROM interviews WHERE(year = 2020 AND month = 7 AND day = 28);

-- license_plates of all suspects
SELECT license_plate FROM courthouse_security_logs WHERE(year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25 AND activity = "exit");

-- account numbers of all suspects
SELECT account_number from atm_transactions WHERE(year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street" AND transaction_type = "withdraw");

-- phone numbers of all suspects
SELECT caller FROM phone_calls WHERE(year = 2020 AND month = 7 AND day = 28 AND duration < 60);

-- phone numbers of all possible accomplices
SELECT receiver FROM phone_calls WHERE(year = 2020 AND month = 7 AND day = 28 AND duration < 60);

-- airport id might be helpful in order to find the flight id
SELECT id FROM airports WHERE full_name = "Fiftyville Regional Airport";

-- flight id
SELECT id FROM flights WHERE(year = 2020 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE full_name = "Fiftyville Regional Airport")) ORDER BY hour, minute LIMIT 1;

-- the city that the thief is escaped to
SELECT city FROM airports WHERE id = (SELECT destination_airport_id FROM flights WHERE(year = 2020 AND month = 7 AND day = 29) ORDER BY hour, minute LIMIT 1);

-- passport_numbers of all suspects
SELECT passport_number FROM passengers WHERE(flight_id = (SELECT id FROM flights WHERE(year = 2020 AND month = 7 AND day = 29 AND origin_airport_id = (SELECT id FROM airports WHERE full_name = "Fiftyville Regional Airport")) ORDER BY hour, minute LIMIT 1) AND passport_number IN(select passport_number from people WHERE license_plate IN(SELECT license_plate FROM courthouse_security_logs WHERE(year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25 AND activity = "exit"))));

-- id numbers of all suspects
SELECT person_id FROM bank_accounts WHERE account_number IN(SELECT account_number from atm_transactions WHERE(year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street" AND transaction_type = "withdraw"));

-- thief
SELECT name FROM people WHERE(id IN(SELECT person_id FROM bank_accounts WHERE account_number IN(SELECT account_number from atm_transactions WHERE(year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street" AND transaction_type = "withdraw"))) AND phone_number IN(SELECT caller FROM phone_calls WHERE(year = 2020 AND month = 7 AND day = 28 AND duration < 60)) AND passport_number IN(SELECT passport_number FROM passengers WHERE(flight_id = (SELECT id FROM flights WHERE(year = 2020 AND month = 7 AND day = 29) ORDER BY hour, minute LIMIT 1) AND passport_number IN(select passport_number from people WHERE license_plate IN(SELECT license_plate FROM courthouse_security_logs WHERE(year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25 AND activity = "exit"))))) AND license_plate IN(SELECT license_plate FROM courthouse_security_logs WHERE(year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25 AND activity = "exit")));

-- thief’s accomplice
SELECT name FROM people WHERE phone_number = (SELECT receiver FROM phone_calls WHERE(year = 2020 AND month = 7 AND day = 28 AND duration < 60 AND caller = (SELECT phone_number FROM people WHERE(id IN(SELECT person_id FROM bank_accounts WHERE account_number IN(SELECT account_number from atm_transactions WHERE(year = 2020 AND month = 7 AND day = 28 AND atm_location = "Fifer Street" AND transaction_type = "withdraw"))) AND phone_number IN(SELECT caller FROM phone_calls WHERE(year = 2020 AND month = 7 AND day = 28 AND duration < 60)) AND passport_number IN(SELECT passport_number FROM passengers WHERE(flight_id = (SELECT id FROM flights WHERE(year = 2020 AND month = 7 AND day = 29) ORDER BY hour, minute LIMIT 1) AND passport_number IN(select passport_number from people WHERE license_plate IN(SELECT license_plate FROM courthouse_security_logs WHERE(year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25 AND activity = "exit"))))) AND license_plate IN(SELECT license_plate FROM courthouse_security_logs WHERE(year = 2020 AND month = 7 AND day = 28 AND hour = 10 AND minute >= 15 AND minute <= 25 AND activity = "exit"))))));