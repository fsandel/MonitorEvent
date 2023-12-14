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

func Fetch(url string, requestType string) ([]byte, error) {
	spaceClient := http.Client{
		Timeout: time.Second * 2,
	}

	req, err := http.NewRequest(requestType, url, nil)
	if err != nil {
		return nil, err
	}
	req.Header["Authorization"] = []string{
		fmt.Sprintf("Bearer %s", token),
	}

	var res *http.Response
	var resErr error
	for {
		res, resErr = spaceClient.Do(req)
		if resErr != nil {
			return nil, resErr
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
		return nil, err
	}

	return body, nil
}

type User struct {
	intraname  string
	image      string
	pool_month string
	pool_year  string
}

// def fetchAllUsers(oauth, returnUsers):
//     returnUsers.clear()
//     amount = 1
//     page = 0
//     while amount > 0:
//         time.sleep(1)
//         response = oauth.get(
//             f"{API_URL}/v2/campus/{HEILBRONN_ID}/users?page={page}")
//         if response.status_code == 200:
//             page += 1
//             data = response.json()
//             for user in data:
//                 returnUsers.append({"userName": user['login'], "userId": user['id'], "userImg": user['image']
//                                    ['link'], "pool_month": user['pool_month'], "pool_year": user['pool_year']})
//             amount = len(data)
//         else:
//             amount = 0

func FetchAllUsers() ([]User, error) {
	var allUsers []User

	url := fmt.Sprintf("https://api.intra.42.fr/v2/campus/39/users?page=%d", 0)
	userPage, err := Fetch(url, http.MethodGet)
	if err != nil {
		return []User{}, err
	}
	var test []map[string]json.RawMessage
	json.Unmarshal(userPage, &test)
	for _, user := range test {
		var newUser User
		newUser.intraname = string(user["login"])
		newUser.pool_month = string(user["pool_month"])
		newUser.pool_year = string(user["pool_year"])
		var nestedJson1, nestedJson2 map[string]json.RawMessage
		json.Unmarshal(user["image"], &nestedJson1)
		json.Unmarshal(nestedJson1["versions"], &nestedJson2)
		newUser.image = string(nestedJson2["large"])
		allUsers = append(allUsers, newUser)
	}
	return allUsers, nil
}
