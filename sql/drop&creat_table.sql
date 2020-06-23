use PokeCorp


DROP table owned;

DROP table trainer;

DROP TABLE pokemon;

DROP TABLE type;

DROP TABLE type_pokemon;


CREATE TABLE pokemon (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(45) DEFAULT NULL,
  type varchar(45) DEFAULT NULL,
  height decimal(10,3) DEFAULT NULL,
  weight decimal(10,3) DEFAULT NULL,
  sprites_back_shiny varchar(45) DEFAULT NULL,
  sprites_front_shiny varchar(45) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1 ;


CREATE TABLE trainer (
  id int(11) NOT NULL AUTO_INCREMENT,
  name varchar(45) DEFAULT NULL,
  town varchar(45) DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin;

CREATE TABLE owned (
  id_pokemon int(11) NOT NULL,
  id_trainer int(11) NOT NULL,
  PRIMARY KEY (id_pokemon,id_trainer),
  CONSTRAINT fk_owned FOREIGN KEY (id_pokemon) REFERENCES pokemon (id) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT fk_owned_1 FOREIGN KEY (id_trainer) REFERENCES trainer (id) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1 ;

CREATE TABLE type (
  name varchar(45) NOT NULL,
  url varchar(45) DEFAULT NULL,
  PRIMARY KEY (name)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE type_pokemon (
  name_type varchar(45) NOT NULL,
  id_pokemon int(11) NOT NULL,
  PRIMARY KEY (name_type,id_pokemon),
  CONSTRAINT fk_type_pokemon_1 FOREIGN KEY (name_type) REFERENCES type (name) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT fk_type_pokemon_2 FOREIGN KEY (id_pokemon) REFERENCES pokemon (id) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;