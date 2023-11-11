import React, { useEffect, useState } from "react";
import Userentry from "../userentry";
import styled from "styled-components";
import { BACKEND } from "../../types/constants";
import { useNavigate } from "react-router-dom";

interface IUser {
  userName: string;
  userId: string;
  userImg?: string;
  registered: boolean;
}

interface IExam {
  examName: string;
}

const UserlistWrapper = styled.div`
  ul {
    list-style: none;
    padding: 0;
  }

  li {
    padding-left: 10px; /* Add padding to the left of each list item */
  }
`;

const Userlist: React.FC = () => {
  const [userData, setUserData] = useState<IUser[]>([]);
  const [exam, setExam] = useState<IExam>();
  const [userAmount, setUserAmount] = useState<number>(0);
  const [userPisciner, setAllPisciner] = useState<number>(0);
  const [userPiscinerInExam, setAllPiscinerInExam] = useState<number>(0);
  const navigate = useNavigate();

  useEffect(() => {
    fetch(`${BACKEND}/getuserdata`)
      .then((res) => res.json())
      .then((data) => setUserData(data))
      .catch(() => console.log("error"));

    fetch(`${BACKEND}/getexam`)
      .then((res) => res.json())
      .then((data) => setExam(data))
      .catch(() => console.log("error"));

    fetch(`${BACKEND}/getuseramount`)
      .then((res) => res.json())
      .then((data) => setUserAmount(data))
      .catch(() => console.log("error"));

    fetch(`${BACKEND}/getallpisciner`)
      .then((res) => res.json())
      .then((data) => setAllPisciner(data))
      .catch(() => console.log("error"));

    fetch(`${BACKEND}/getallpiscinerinexam`)
      .then((res) => res.json())
      .then((data) => setAllPiscinerInExam(data))
      .catch(() => console.log("error"));
  }, []);

  console.log(userData);
  // @app.route("/getallpisciner")
  // def getallpisciner():
  //     return jsonify(len(allPisciners))

  // @app.route("/getallpiscinerinexam")
  return (
    <UserlistWrapper>
      <h1>{exam?.examName}</h1>
      <h2>useramount: {userAmount}</h2>
      <h2>allpiscner: {userPisciner}</h2>
      <h2>PiscinerInExam: {userPiscinerInExam}</h2>
      <ul>
        {userData.map((element: IUser, index) => (
          <div
            onClick={() => {
              navigate(`/user/${element.userId}`);
            }}
          >
            <li key={index}>
              <Userentry user={element} />
            </li>
          </div>
        ))}
      </ul>
    </UserlistWrapper>
  );
};

export default Userlist;
