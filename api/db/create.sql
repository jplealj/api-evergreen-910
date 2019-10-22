CREATE TABLE `evergreen`.`mediciones` (
  `fecha` DATETIME NOT NULL,
  `origen` VARCHAR(100) NOT NULL,
  `valor` INT NULL,
  `codigoSensor` INT NOT NULL,
  `observacion` VARCHAR(100) NULL);
