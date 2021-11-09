CREATE TABLE `character` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    `name` TEXT,
    `playerId` TEXT,
    `characterClass` TEXT,
    'level' INTEGER,
    'xp' INTEGER,
    'gold' INTEGER,
    'inventory' TEXT,
    'goalsCompleted' INTEGER
);