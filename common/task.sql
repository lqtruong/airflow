CREATE TABLE todos.task (
	id BIGINT auto_increment NOT NULL,
	name varchar(100) NOT NULL,
	`desc` varchar(500) NULL,
	person_id varchar(100) NOT NULL,
	created_at DATETIME NULL,
	updated_at DATETIME NULL,
	m_id varchar(100) NOT NULL,
	CONSTRAINT task_PK PRIMARY KEY (id)
)
ENGINE=InnoDB
DEFAULT CHARSET=latin1
COLLATE=latin1_swedish_ci;
