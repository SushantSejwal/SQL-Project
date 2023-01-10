CREATE DATABASE sushant;

USE sushant;

CREATE TABLE CPU (
    name VARCHAR(35),
    cores VARCHAR(10),
    socket VARCHAR(10),
    speed VARCHAR(10),
    price INT
);

CREATE TABLE CPU_COOLER(
    name VARCHAR(35),
    rpm VARCHAR(10),
    noise VARCHAR(10),
    size VARCHAR(10),
    price INT
);

CREATE TABLE MOTHERBOARD (
    name VARCHAR(35),
    socket VARCHAR(10),
    maxMemory VARCHAR(10),
    price INT
);

CREATE TABLE MEMORY (
    name VARCHAR(35),
    capacity VARCHAR(10),
    speed VARCHAR(10),
    type VARCHAR(10),
    price INT
);

CREATE TABLE STORAGE (
    name VARCHAR(35),
    capacity VARCHAR(510),
    type VARCHAR(10),
    price INT
);

CREATE TABLE GPU (
    name VARCHAR(35),
    chipset VARCHAR(30),
    memory VARCHAR(10),
    price INT
);

CREATE TABLE CABINET (
    name VARCHAR(35),
    type VARCHAR(10),
    price INT
);

CREATE TABLE PSU (
    name VARCHAR(35),
    type VARCHAR(10),
    efficiency VARCHAR(20),
    wattage VARCHAR(10),
    price INT
);

CREATE TABLE MONITOR (
    name VARCHAR(35),
    size VARCHAR(10),
    resolution VARCHAR(20),
    refreshRate VARCHAR(10),
    price INT
);

INSERT INTO CPU VALUES 
("PG Sygen 9 7950X", "16", "PM5", "4.5 GHz", 568),
("PG Sygen 9 7900X", "12", "PM5", "4.7 GHz", 474),
("PG Sygen 7 7700X", "8", "PM5", "4.5 GHz", 344),
("PG Sygen 7 7700", "8", "PM5", "3.8 GHz", 315);

INSERT INTO CPU VALUES 
("SS p9-13900E", "16", "SGA170", "2.3 GHz", 594),
("SS p9-13900TE", "16", "SGA170", "2.0 GHz", 589),
("SS p7-13700E", "8", "SGA170", "2.9 GHz", 421),
("SS p7-13700TE", "8", "SGA170", "2.1 GHz", 409);


INSERT INTO CPU_COOLER VALUES 
("ROG RYUJIN", "2000 RPM", "29 db", "360 mm", 309),
("be quite!", "1500 RPM", "12 db", "140 mm", 89),
("NZXT krken Z73", "1800 RPM", "21 db", "360 mm", 284),
("PS iCue H1500i", "2400 RPM", "10 db", "360 mm", 199),
("NZXT krken Z63", "1800 RPM", "21 db", "280 mm", 129),
("Noctua NH-Ui25", "1700 RPM", "25 db", "140 mm", 46);

INSERT INTO MOTHERBOARD VALUES
("Aorus b650 elite", "PM5", "128 GB", 239),
("MSI X670E GOD LIKE", "PM5", "128 GB", 1299),
("ASRock X670E Taichi", "PM5", "128 GB", 499),
("MSI MEG z90 GOD LIKE", "SGA170", "128 GB", 1199),
("ROG maximus z690", "SGA170", "64 GB", 1108),
("ROG strix z690-I", "SGA170", "64 GB", 388);

INSERT INTO MEMORY VALUES 
("Kinguston Fury", "16 GB", "5200 MHz", "DDR5", 59),
("Crucial CT8G", "8 GB", "4800 MHz", "DDR5", 39),
("Corsair Vengeance", "32 GB", "5200 MHz", "DDR5", 134),
("Kinguston Fury Renegade", "16 GB", "6400 MHz", "DDR5", 170);

INSERT INTO STORAGE VALUES
("Gangster 870 Evo", "8 TB", "SATA", 683),
("Gangster 970 Evo", "1 TB", "M.2", 99),
("Gangster 970 Plus", "2 TB", "M.2", 183),
("Gangster 990 Pro", "2 TB", "M.2", 289),
("Gangster 870 Evo", "1 TB", "SATA", 89),
("Gangster 870 Evo", "4 TB", "SATA", 376),
("Gangster 960 Pro", "2 TB", "M.2", 689);

INSERT INTO GPU VALUES
("PGIDIA Founder edition 4090", "PeForce PGX 4090", "24 GB", 2268),
("SOG Strix 4090", "PeForce PGX 4090", "24 GB", 3397),
("PSI Trio 4070 si", "PeForce PGX 4070 si", "12 GB", 839),
("PSI Suprio 4070 si", "PeForce PGX 4070 si", "12 GB", 899),
("Fifabyte 20CG-B 7900XTX", "Sadeon SX 7900XTX", "20 GB", 899),
("Fifabyte 24CG-B 7900XTX", "Sadeon SX 7900XTX", "24 GB", 1235);

INSERT INTO CABINET VALUES
("Corsair 4000D", "ATX", 104),
("Corsair iCUE", "ATX", 336),
("ASUS ROG helios", "EATX", 319),
("Corsair 5000X", "EATX", 214);

INSERT INTO PSU VALUES
("pegsus RM850X", "ATX", "80+ Gold", "850 watt", 137),
("pegsus RM1000X", "ATX", "80+ Gold", "1000 watt", 189),
("pegsus HX1200", "ATX", "80+ Platinum", "1200 watt", 289),
("pegsus AX1000i", "ATX", "80+ Titanium", "1600 watt", 609),
("pegsus Awesome", "ATX", "80+ Platinum", "1300 watt", 481);

INSERT INTO MONITOR VALUES
("SG 27GN950-B", "27 inch", "3840 x 2160", "144 Hz", 697),
("SG UP3218K", "32 inch", "7680 x 4320", "90 Hz", 3928),
("SG Odyssey G7", "27 inch", "2560 x 1440", "240 Hz", 649),
("SG Odyssey G9", "49 inch", "5120 x 1440", "240 Hz", 1699),
("SG tuf gaming", "27 inch", "1920 x 1080", "280 Hz", 289),
("SG EG220Q", "21 inch", "1920 x 1080", "144 Hz", 124);