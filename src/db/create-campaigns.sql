CREATE TABLE IF NOT EXISTS `campaign` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    `name` TEXT,
    'gameMasterId' INTEGER, -- Must map to an player.id!
    `missionsCompleted` TEXT,
    `missionsAvailable` TEXT,
    'eventsCompleted' TEXT,
    'itemsAvailable' TEXT,
    'characters' TEXT,
    FOREIGN KEY(gameMasterId) REFERENCES player(id)
);