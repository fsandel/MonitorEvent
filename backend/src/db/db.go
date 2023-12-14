package db

import (
	"database/sql"

	_ "github.com/lib/pq"
)

func Setup() error {
	connStr := "postgresql://root:testpwd@localhost:5432/monitor?sslmode=disable"
	db, err := sql.Open("postgres", connStr)
	if err != nil {
		return err
	}

	err = setupUserTable(db)
	if err != nil {
		return err
	}

	return nil
}

func setupUserTable(db *sql.DB) error {
	_, err := db.Exec(`CREATE TABLE IF NOT EXISTS users (
												intraname VARCHAR(255) NOT NULL UNIQUE,
												image VARCHAR(255) NOT NULL,
												pool_month VARCHAR(255) NOT NULL,
												pool_year VARCHAR(255) NOT NULL
	)`)
	if err != nil {
		return err
	}

	return nil
}
