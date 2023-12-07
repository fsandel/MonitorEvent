package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"time"
)

func getToken() (string, error) {

	UID := os.Getenv("USERID")
	SECRET := os.Getenv("SECRET")
	url := fmt.Sprintf("https://api.intra.42.fr/oauth/token?grant_type=client_credentials&client_id=%s&client_secret=%s", UID, SECRET)

	spaceClient := http.Client{
		Timeout: time.Second * 2,
	}
	req, err := http.NewRequest(http.MethodPost, url, nil)
	if err != nil {
		return "", err
	}

	res, getErr := spaceClient.Do(req)
	if getErr != nil {
		return "", getErr
	}
	defer res.Body.Close()

	body, readErr := io.ReadAll(res.Body)
	if readErr != nil {
		return "", readErr
	}

	var bodyMap map[string]string
	json.Unmarshal([]byte(body), &bodyMap)

	return bodyMap["access_token"], nil
}

func main() {
	token, tokenErr := getToken()
	if tokenErr != nil {
		log.Fatal(tokenErr)
	}
	fmt.Println(token)
}
