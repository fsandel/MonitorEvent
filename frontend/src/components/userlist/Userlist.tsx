import React, { useEffect, useState } from "react";
import Userentry from "../userentry";

interface IUser {
  userName: string;
  userId: string;
}

const Userlist: React.FC = () => {
  const [userData, setUserData] = useState<IUser[]>([]);

  useEffect(() => {
    fetch("http://localhost:4000/raw")
      .then((res) => res.json())
      .then((data) => setUserData(data))
      .catch(() => console.log("error"));
  }, []);

  console.log(userData);

  return (
    <div>
      <h1>User List</h1>
      <ul>
        {userData.map((element: IUser, index) => (
          <li key={index}>
            <Userentry user={element} />
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Userlist;
