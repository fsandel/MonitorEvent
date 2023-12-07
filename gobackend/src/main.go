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

func fetch(url string, token string, requestType string) (string, error) {
	spaceClient := http.Client{
		Timeout: time.Second * 2,
	}

	req, err := http.NewRequest(requestType, url, nil)
	if err != nil {
		return "", err
	}
	req.Header["Authorization"] = []string{
		fmt.Sprintf("Bearer %s", token),
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

	return string(body), nil
}

func main() {
	token, tokenErr := getToken()
	if tokenErr != nil {
		log.Fatal(tokenErr)
	}

	body, err := fetch("https://api.intra.42.fr/v2/users/fsandel", token, http.MethodGet)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(body)
}
