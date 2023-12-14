package main

import (
	"log"
	"main/db"
)

// func test() {
// 	body, err := intra.FetchAllUsers()
// 	if err != nil {
// 		log.Fatal(err)
// 	}
// 	fmt.Println(body)
// }

func main() {
	// err := intra.GetToken()
	// if err != nil {
	// 	log.Fatal(err)
	// }

	err := db.Setup()
	if err != nil {
		log.Fatal(err)
	}
}
