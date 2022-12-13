# List of tables
# members - list of all users and band members
# bands - list of all bands using this appliation
# band_members - defines who is member of which band
# nogo_dates - nogo-dates of members

DROP TABLE IF EXISTS members;
CREATE TABLE members(name TEXT, name_full TEXT, password TEXT, enabled BOOLEAN);
INSERT INTO members(name, name_full, password, enabled) VALUES ('santtu','Santtu Salmiakki','sala', TRUE);
INSERT INTO members(name, name_full, password, enabled) VALUES ('lipa','Lippa Vika','sala', TRUE);
INSERT INTO members(name, name_full, password, enabled) VALUES ('baasi','Basse Bom','sala', TRUE);
INSERT INTO members(name, name_full, password, enabled) VALUES ('rumppi','Rane Rump','sala', TRUE);
INSERT INTO members(name, name_full, password, enabled) VALUES ('kilju','Kille Kulju','sala', TRUE);

DROP TABLE IF EXISTS bands;
CREATE TABLE bands(name TEXT, name_full TEXT);
INSERT INTO bands(name, name_full) VALUES ('KM','Kaikki mukaan');
INSERT INTO bands(name, name_full) VALUES ('HP','Hevon Humppa');
INSERT INTO bands(name, name_full) VALUES ('P3','Paskaa kolmannella');
INSERT INTO bands(name, name_full) VALUES ('LoL','Lievästi on liukasta');

DROP TABLE IF EXISTS band_members;
CREATE TABLE band_members(band_name TEXT, member_name TEXT);
INSERT INTO band_members(band_name, member_name) VALUES ('KM','santtu');
INSERT INTO band_members(band_name, member_name) VALUES ('KM','lippa');
INSERT INTO band_members(band_name, member_name) VALUES ('KM','baasi');
INSERT INTO band_members(band_name, member_name) VALUES ('KM','rumppi');
INSERT INTO band_members(band_name, member_name) VALUES ('KM','kilju');

INSERT INTO band_members(band_name, member_name) VALUES ('HP','santtu');
INSERT INTO band_members(band_name, member_name) VALUES ('HP','lippa');
INSERT INTO band_members(band_name, member_name) VALUES ('HP','baasi');

INSERT INTO band_members(band_name, member_name) VALUES ('P3','baasi');
INSERT INTO band_members(band_name, member_name) VALUES ('P3','rumppi');
INSERT INTO band_members(band_name, member_name) VALUES ('P3','kilju');

INSERT INTO band_members(band_name, member_name) VALUES ('LoL','lippa');
INSERT INTO band_members(band_name, member_name) VALUES ('LoL','rumppi');


DROP TABLE IF EXISTS nogo_dates;
CREATE TABLE nogo_dates(date DATE, member_name TEXT);
INSERT INTO nogo_dates(date, member_NAME) VALUES ('2022-06-11', 'lipa');
INSERT INTO nogo_dates(date, member_NAME) VALUES ('2022-05-12', 'rumppi');
INSERT INTO nogo_dates(date, member_NAME) VALUES ('2022-02-20', 'santtu');
INSERT INTO nogo_dates(date, member_NAME) VALUES ('2022-05-12', 'baasi');
INSERT INTO nogo_dates(date, member_NAME) VALUES ('2022-04-01', 'kilju');
INSERT INTO nogo_dates(date, member_NAME) VALUES ('2022-05-14', 'rumppi');

.dump


