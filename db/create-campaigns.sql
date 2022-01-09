CREATE TABLE IF NOT EXISTS `campaign` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    `name` TEXT,
    `missionsCompleted` TEXT,
    `missionsAvailable` TEXT,
    'eventsCompleted' TEXT,
    'itemsAvailable' TEXT
);