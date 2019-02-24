DROP TABLE IF EXISTS submission;
DROP TABLE IF EXISTS cranks;

CREATE TABLE Submission (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Username TEXT NOT NULL,
  Expname TEXT NOT NULL,  
  Crank TEXT NOT NULL,  
  Filename TEXT NOT NULL,
  Notes TEXT,
  Created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE Cranks (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  Crank TEXT NOT NULL,
  Stateset TEXT NOT NULL,
  Filename TEXT NOT NULL,
  Gitcommit TEXT NOT NULL,
  Current BOOL DEFAULT FALSE,
  Created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO Cranks (Crank,Stateset,Filename,Gitcommit,Current,Created) VALUES ("0001", "aaaaaaaaaaa","0001.csv","abc1111",'FALSE','2019-02-19 05:04:56.200');
INSERT INTO Cranks (Crank,Stateset,Filename,Gitcommit,Current,Created) VALUES ("0002", "aaaaaaaaaab","0001.csv","abc2222",'FALSE','2019-02-20 10:20:56.200');
INSERT INTO Cranks (Crank,Stateset,Filename,Gitcommit,Current,Created) VALUES ("0002", "aaaaaaaaaac","0002.csv","abc3333",'TRUE', '2019-02-21 15:18:56.200');

INSERT into Submission (Username, Expname, Crank, Filename, Notes) VALUES ("snovot","first","0001","abc.csv","test test");
INSERT into Submission (Username, Expname, Crank, Filename, Notes) VALUES ("snovot","second","0001","abc1.csv","test test");
INSERT into Submission (Username, Expname, Crank, Filename, Notes) VALUES ("snovot","third","0002","abc2.csv","test test");
INSERT into Submission (Username, Expname, Crank, Filename, Notes) VALUES ("snovot","fourth","0002","abc3.csv","test test");
