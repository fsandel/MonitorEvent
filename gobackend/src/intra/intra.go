package intra

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"time"
)

var token string

func GetToken() error {

	UID := os.Getenv("USERID")
	SECRET := os.Getenv("SECRET")
	url := fmt.Sprintf("https://api.intra.42.fr/oauth/token?grant_type=client_credentials&client_id=%s&client_secret=%s", UID, SECRET)

	spaceClient := http.Client{
		Timeout: time.Second * 2,
	}

	req, err := http.NewRequest(http.MethodPost, url, nil)
	if err != nil {
		return err
	}

	res, err := spaceClient.Do(req)
	if err != nil {
		return err
	}

	defer res.Body.Close()
	body, err := io.ReadAll(res.Body)
	if err != nil {
		return err
	}

	var bodyMap map[string]string
	json.Unmarshal([]byte(body), &bodyMap)
	token = bodyMap["access_token"]

	return nil
}

func Fetch(url string, requestType string) (string, error) {
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

	var res *http.Response
	var resErr error
	for {
		res, resErr = spaceClient.Do(req)
		if resErr != nil {
			return "", resErr
		}
		if res.StatusCode == 429 {
			time.Sleep(time.Millisecond * 300)
		} else {
			break
		}
	}

	defer res.Body.Close()
	body, err := io.ReadAll(res.Body)
	if err != nil {
		return "", err
	}

	return string(body), nil
}
