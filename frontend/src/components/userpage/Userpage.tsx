import React, { useEffect, useState } from "react";
import { BACKEND } from "../../types/constants";
import { useParams } from "react-router-dom";
import Userimage from "../userimage";

interface IProfile {
  userName: string;
  userImg: string;
  exams: string[];
  projects: string[];
}

const Userpage: React.FC = () => {
  const { userId } = useParams();
  const [profileData, setProfileData] = useState<IProfile>({
    userName: "",
    exams: [],
    projects: [],
    userImg: "",
  });

  useEffect(() => {
    console.log(`userid:${userId}:`);
    fetch(`${BACKEND}/user/${userId}`)
      .then((response) => response.json())
      .then((data) => setProfileData(data))
      .catch((error) => {
        console.error("get event failed", error);
      });
  }, [userId]);
  return (
    <>
      <div>
        <div>
          <h1>{profileData.userName}</h1>
          <p></p>
          <h2>Exams</h2>
          <ul>
            {profileData.exams.map((element: string, index) => (
              <li key={index}>
                <p>{element}</p>
              </li>
            ))}
          </ul>
        </div>
        <div>
          <p></p>
          <h2>Projects</h2>
          <ul>
            {profileData.projects.map((element: string, index) => (
              <li key={index}>
                <p>{element}</p>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </>
  );
};

export default Userpage;
