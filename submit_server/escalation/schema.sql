DROP TABLE IF EXISTS submission;

CREATE TABLE submission (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  crank TEXT NOT NULL,  
  filename TEXT NOT NULL,
  notes TEXT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

