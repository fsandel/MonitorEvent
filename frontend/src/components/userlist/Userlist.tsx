import React, { useEffect, useState } from "react";
import Userentry from "../userentry";
import styled from "styled-components";

interface IUser {
  userName: string;
  userId: string;
  userImg?: string;
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

  useEffect(() => {
    fetch("http://localhost:4000/pictures")
      .then((res) => res.json())
      .then((data) => setUserData(data))
      .catch(() => console.log("error"));
  }, []);

  console.log(userData);

  return (
    <UserlistWrapper>
      <h1>User List</h1>
      <ul>
        {userData.map((element: IUser, index) => (
          <li key={index}>
            <Userentry user={element} />
          </li>
        ))}
      </ul>
    </UserlistWrapper>
  );
};

export default Userlist;
