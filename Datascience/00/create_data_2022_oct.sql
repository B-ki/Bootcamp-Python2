DROP TABLE IF EXISTS data_2022_oct;
CREATE TABLE data_2022_oct (
	id BIGSERIAL PRIMARY KEY,
	event_time TIMESTAMP,
	event_type VARCHAR(50),
	product_id INTEGER NOT NULL,
	price FLOAT,
	user_id BIGINT NOT NULL,
	user_session VARCHAR(100)
);

COPY data_2022_oct(event_time, event_type, product_id, price, user_id, user_session)
FROM '/var/lib/postgresql/data/subject/customer/data_2022_oct.csv'
DELIMITER ','
CSV HEADER;
