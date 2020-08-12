-- Getting to know the table 
SELECT * FROM stream LIMIT 20;
SELECT * FROM chat LIMIT 20;

-- List of all game in twitch
SELECT DISTINCT game FROM stream;

-- List of channel in twitch
SELECT DISTINCT channel FROM stream;

-- Most popular game in twitch
SELECT game, COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 2 DESC;

-- Countries from LoL player
SELECT country, COUNT(*)
FROM stream
WHERE game == 'League of Legends'
GROUP BY 1
ORDER BY 2 DESC;

-- Source of streamer
SELECT player, COUNT(*) 
FROM stream
GROUP BY 1
ORDER BY 2 DESC;

-- Game and genre of twitch
SELECT game, 
  CASE
    WHEN game = 'Dota 2'
      THEN 'MOBA'
  WHEN game = 'League of Legends' 
      THEN 'MOBA'
  WHEN game = 'Heroes of the Storm'
      THEN 'MOBA'
    WHEN game = 'Counter-Strike: Global Offensive'
      THEN 'FPS'
    WHEN game = 'DayZ'
      THEN 'Survival'
    WHEN game = 'ARK: Survival Evolved'
      THEN 'Survival'
  ELSE 'Other'
  END AS 'genre',
  COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 3 DESC;

-- Total streamer in every hours from Indonesia
SELECT strftime('%H', time) AS 'Hours', COUNT(*)
FROM stream
WHERE country = 'ID'
GROUP BY 1;

-- Joining stream and chat table 
SELECT *
FROM stream
JOIN chat
  ON stream.device_id = chat.device_id;