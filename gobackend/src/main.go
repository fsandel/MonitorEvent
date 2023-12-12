package main

import (
	"fmt"
	"log"
	"main/intra"
	"net/http"
)

func test() {
	body, err := intra.Fetch("https://api.intra.42.fr/v2/users/fsandel", http.MethodGet)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(body)
}

func main() {
	err := intra.GetToken()
	if err != nil {
		log.Fatal(err)
	}

	test()
	test()
	test()
	test()
	test()
	test()
	test()
	test()

}
