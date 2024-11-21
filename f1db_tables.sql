#USE f1db;

CREATE TABLE `circuits` (
  `circuitId` int(11) NOT NULL AUTO_INCREMENT,
  `circuitRef` varchar(255) NOT NULL DEFAULT '',
  `name` varchar(255) NOT NULL DEFAULT '',
  `location` varchar(255) DEFAULT NULL,
  `country` varchar(255) DEFAULT NULL,
  `alt` int(11) DEFAULT NULL,
  PRIMARY KEY (`circuitId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `constructorStandings` (
  `constructorStandingsId` int(11) NOT NULL AUTO_INCREMENT,
  `raceId` int(11) NOT NULL DEFAULT '0',
  `constructorId` int(11) NOT NULL DEFAULT '0',
  `points` float NOT NULL DEFAULT '0',
  `position` int(11) DEFAULT NULL,
  `positionText` varchar(255) DEFAULT NULL,
  `wins` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`constructorStandingsId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `constructors` (
  `constructorId` int(11) NOT NULL AUTO_INCREMENT,
  `constructorRef` varchar(255) NOT NULL DEFAULT '',
  `name` varchar(255) NOT NULL DEFAULT '',
  `nationality` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`constructorId`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `driverStandings` (
  `driverStandingsId` int(11) NOT NULL AUTO_INCREMENT,
  `raceId` int(11) NOT NULL DEFAULT '0',
  `driverId` int(11) NOT NULL DEFAULT '0',
  `points` float DEFAULT '0',
  `position` int(11) DEFAULT NULL,
  `positionText` varchar(255) DEFAULT NULL,
  `wins` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`driverStandingsId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `drivers` (
  `driverId` int(11) NOT NULL AUTO_INCREMENT,
  `driverRef` varchar(255) NOT NULL DEFAULT '',
  `number` int(11) DEFAULT NULL,
  `code` varchar(3) DEFAULT NULL,
  `Name` varchar(255) NOT NULL DEFAULT '',
  `dob` datetime DEFAULT NULL,
  `nationality` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`driverId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `lapTimes` (
  `raceId` int(11) NOT NULL,
  `driverId` int(11) NOT NULL,
  `lap` int(11) NOT NULL,
  `position` int(11) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`raceId`,`driverId`,`lap`),
  KEY `raceId` (`raceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `pitStops` (
  `raceId` int(11) NOT NULL,
  `driverId` int(11) NOT NULL,
  `stop` int(11) NOT NULL,
  `lap` int(11) NOT NULL,
  `duration` varchar(255) DEFAULT NULL,
  `milliseconds` int(11) DEFAULT NULL,
  PRIMARY KEY (`raceId`,`driverId`,`stop`),
  KEY `raceId` (`raceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `qualifying` (
  `qualifyId` int(11) NOT NULL AUTO_INCREMENT,
  `raceId` int(11) NOT NULL DEFAULT '0',
  `driverId` int(11) NOT NULL DEFAULT '0',
  `constructorId` int(11) NOT NULL DEFAULT '0',
  `number` int(11) DEFAULT '0',
  `position` int(11) DEFAULT NULL,
  `q1` varchar(255) DEFAULT NULL,
  `q2` varchar(255) DEFAULT NULL,
  `q3` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`qualifyId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `races` (
  `raceId` int(11) NOT NULL AUTO_INCREMENT,
  `year` int(11) NOT NULL DEFAULT '0',
  `round` int(11) NOT NULL DEFAULT '0',
  `circuitId` int(11) NOT NULL DEFAULT '0',
  `name` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`raceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `results` (
  `resultId` int(11) NOT NULL AUTO_INCREMENT,
  `raceId` int(11) NOT NULL DEFAULT '0',
  `driverId` int(11) NOT NULL DEFAULT '0',
  `constructorId` int(11) NOT NULL DEFAULT '0',
  `number` int(11) DEFAULT NULL,
  `grid` int(11) DEFAULT NULL,
  `position` int(11) DEFAULT NULL,
  `positionText` varchar(255) DEFAULT '',
  `points` float DEFAULT '0',
  `laps` int(11) DEFAULT NULL,
  `time` varchar(255) DEFAULT NULL,
  `fastestLapTime` varchar(255) DEFAULT NULL,
  `statusId` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`resultId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `seasons` (
  `year` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`year`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `sprintResults` (
  `sprintResultId` int(11) NOT NULL AUTO_INCREMENT,
  `raceId` int(11) NOT NULL DEFAULT '0',
  `driverId` int(11) NOT NULL DEFAULT '0',
  `constructorId` int(11) NOT NULL DEFAULT '0',
  `number` int(11) NOT NULL DEFAULT '0',
  `grid` int(11) NOT NULL DEFAULT '0',
  `position` int(11) DEFAULT NULL,
  `positionText` varchar(255) NOT NULL DEFAULT '',
  `points` float NOT NULL DEFAULT '0',
  `laps` int(11) NOT NULL DEFAULT '0',
  `time` varchar(255) DEFAULT NULL,
  `fastestLapTime` varchar(255) DEFAULT NULL,
  `statusId` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`sprintResultId`),
  KEY `raceId` (`raceId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `status` (
  `statusId` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`statusId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `user` (
  `userId` varchar(255) NOT NULL UNIQUE DEFAULT '',
  `userPw` varchar(255) NOT NULL DEFAULT '',
  `userName` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

