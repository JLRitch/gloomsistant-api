CREATE TABLE IF NOT EXISTS `perks` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    `characterId` INTEGER,
    'perkDesc' TEXT,
    'perkLevel' INTEGER
);