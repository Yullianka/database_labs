-- Таблиця billing_account (must be first - no dependencies)
INSERT IGNORE INTO billing_account (id, balance, account_number) VALUES
(1, '120', 'BA001_NEW'),
(2, '120', 'BA002_NEW'),
(3, '120', 'BA003_NEW'),
(4, '120', 'BA004_NEW'),
(5, '120', 'BA005_NEW'),
(6, '120', 'BA006_NEW'),
(7, '120', 'BA007_NEW'),
(8, '120', 'BA008_NEW'),
(9, '120', 'BA009_NEW'),
(10, '120', 'BA010_NEW');

-- Таблиця solar_station (depends on billing_account)
INSERT IGNORE INTO solar_station (id, name, household, billing_account_id) 
VALUES 
(1, 'Station A', 1, 1),
(2, 'Station B', 2, 2),
(3, 'Station C', 3, 3),
(4, 'Station D', 4, 4),
(5, 'Station E', 5, 5),
(6, 'Station F', 6, 6),
(7, 'Station G', 7, 7),
(8, 'Station H', 8, 8),
(9, 'Station I', 9, 9),
(10, 'Station J', 10, 10);

-- Таблиця users (depends on solar_station)
INSERT IGNORE INTO users (id, name, contact_info, amount_of_station, solar_station_id) 
VALUES 
(1, 'User 1', 'user1@example.com', 1, 1),
(2, 'User 2', 'user2@example.com', 2, 2),
(3, 'User 3', 'user3@example.com', 1, 3),
(4, 'User 4', 'user4@example.com', 3, 4),
(5, 'User 5', 'user5@example.com', 4, 5),
(6, 'User 6', 'user6@example.com', 2, 6),
(7, 'User 7', 'user7@example.com', 1, 7),
(8, 'User 8', 'user8@example.com', 5, 8),
(9, 'User 9', 'user9@example.com', 3, 9),
(10, 'User 10', 'user10@example.com', 4, 10);

-- Таблиця households (depends on users and solar_station)
INSERT IGNORE INTO households (id, address, users_id, solar_station_id) 
VALUES 
(1, 'Address 1', 1, 1),
(2, 'Address 2', 2, 1),
(3, 'Address 3', 3, 2),
(4, 'Address 4', 4, 3),
(5, 'Address 5', 5, 4),
(6, 'Address 6', 6, 5),
(7, 'Address 7', 7, 6),
(8, 'Address 8', 8, 7),
(9, 'Address 9', 9, 8),
(10, 'Address 10', 10, 9);

-- Таблиця users_has_solar_station (depends on users and solar_station)
INSERT IGNORE INTO users_has_solar_station (users_id, solar_station_id) 
VALUES 
(1, 1),
(2, 1),
(3, 2),
(4, 3),
(5, 4),
(6, 5),
(7, 6),
(8, 7),
(9, 8),
(10, 9);

-- Таблиця panel (depends on solar_station)
INSERT IGNORE INTO panel (id, type, power, installation_date, solar_station_id)
VALUES 
(1, 'Type1', '200W', '2023-10-01', 1),
(2, 'Type2', '300W', '2023-10-05', 2),
(3, 'Type3', '250W', '2023-10-10', 3),
(4, 'Type4', '400W', '2023-10-12', 4),
(5, 'Type5', '350W', '2023-10-15', 5),
(6, 'Type6', '220W', '2023-10-20', 6),
(7, 'Type7', '330W', '2023-10-22', 7),
(8, 'Type8', '310W', '2023-10-25', 8),
(9, 'Type9', '340W', '2023-10-28', 9),
(10, 'Type10', '320W', '2023-10-30', 10);

-- Таблиця battery (depends on solar_station)
INSERT IGNORE INTO battery (id, station_id, capacity, usage_duration, solar_station_id) 
VALUES 
(1, 1, '1000Ah', '5 hours', 1),
(2, 2, '1500Ah', '4 hours', 2),
(3, 3, '1200Ah', '6 hours', 3),
(4, 4, '1800Ah', '5 hours', 4),
(5, 5, '1600Ah', '6 hours', 5),
(6, 6, '1400Ah', '7 hours', 6),
(7, 7, '1700Ah', '5 hours', 7),
(8, 8, '1100Ah', '4 hours', 8),
(9, 9, '1300Ah', '6 hours', 9),
(10, 10, '1550Ah', '7 hours', 10);

-- Таблиця energy_sales (depends on solar_station)
INSERT IGNORE INTO energy_sales (id, timestamp, energy_sold, price_per_kw, energy_selected, solar_station_id)
VALUES
(1, '2023-10-01 12:00:00', '100kWh', '0.12', '80kWh', 1),
(2, '2023-10-01 12:30:00', '150kWh', '0.10', '100kWh', 2),
(3, '2023-10-01 13:00:00', '200kWh', '0.15', '120kWh', 3),
(4, '2023-10-01 13:30:00', '250kWh', '0.11', '90kWh', 4),
(5, '2023-10-01 14:00:00', '300kWh', '0.14', '140kWh', 5),
(6, '2023-10-01 14:30:00', '350kWh', '0.13', '110kWh', 6),
(7, '2023-10-01 15:00:00', '400kWh', '0.12', '130kWh', 7),
(8, '2023-10-01 15:30:00', '450kWh', '0.10', '150kWh', 8),
(9, '2023-10-01 16:00:00', '500kWh', '0.15', '160kWh', 9),
(10, '2023-10-01 16:30:00', '550kWh', '0.14', '170kWh', 10);

-- Таблиця tilt_angles (depends on panel)
INSERT IGNORE INTO tilt_angles (id, timestamp, tilt_angle, panel_id) 
VALUES 
(1, '2023-10-01 08:00:00', '30', 1),
(2, '2023-10-01 09:00:00', '30', 1),
(3, '2023-10-01 10:00:00', '30', 1),
(4, '2023-10-01 08:00:00', '25', 2),
(5, '2023-10-01 09:00:00', '25', 2),
(6, '2023-10-01 10:00:00', '25', 2),
(7, '2023-10-01 08:00:00', '20', 3),
(8, '2023-10-01 09:00:00', '20', 3),
(9, '2023-10-01 10:00:00', '20', 3),
(10, '2023-10-01 08:00:00', '15', 4);

-- Таблиця battery_charge (depends on battery)
INSERT IGNORE INTO battery_charge (id, timestamp, charge_level_per_hour, date, time, battery_id) 
VALUES 
(1, '2023-10-01 08:00:00', '50%', '2023-10-01', '08:00', 1),
(2, '2023-10-01 09:00:00', '60%', '2023-10-01', '09:00', 1),
(3, '2023-10-01 10:00:00', '55%', '2023-10-01', '10:00', 1),
(4, '2023-10-02 08:00:00', '65%', '2023-10-02', '08:00', 2),
(5, '2023-10-02 09:00:00', '70%', '2023-10-02', '09:00', 2),
(6, '2023-10-02 10:00:00', '75%', '2023-10-02', '10:00', 2),
(7, '2023-10-03 08:00:00', '50%', '2023-10-03', '08:00', 3),
(8, '2023-10-03 09:00:00', '55%', '2023-10-03', '09:00', 3),
(9, '2023-10-03 10:00:00', '60%', '2023-10-03', '10:00', 3),
(10, '2023-10-04 08:00:00', '65%', '2023-10-04', '08:00', 4);
