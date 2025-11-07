SELECT palya.ut
FROM palya JOIN europa ON europa.ut=palya.ut
WHERE europa.eurout LIKE "E%5";