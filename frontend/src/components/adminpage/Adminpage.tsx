import React, { useEffect, useState } from "react";
import { BACKEND } from "../../types/constants";

interface IExam {
  examName: string;
}

const Adminpage: React.FC = () => {
  const [localExamName, setLocalExamName] = useState("");
  const [currentExam, setCurrentExam] = useState("");
  const [eventComponentKey, setEventComponentKey] = useState(0);
  const [year, setYear] = useState("");
  const [month, setMonth] = useState("");

  const changeExam = () => {
    fetch(`${BACKEND}/setexam`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(localExamName),
    })
      .then((response) => {
        console.log("POST request successful");
        setCurrentExam(localExamName);
        setEventComponentKey((prevKey) => prevKey + 1);
      })
      .catch((error) => {
        console.error("Error making POST request:", error);
      });
  };

  const refreshData = () => {
    fetch(`${BACKEND}/refresh`, {
      method: "POST",
      headers: {
        "Content-Type": "application json",
      },
      body: JSON.stringify({ eventId: localExamName }),
    })
      .then((response) => {
        console.log("POST request successful");
      })
      .catch((error) => {
        console.error("Error making POST request:", error);
      });
  };

  const fetchExam = () => {
    fetch(`${BACKEND}/getexam`)
      .then((response) => response.json())
      .then((data: IExam) => setCurrentExam(data.examName))
      .catch((error) => {
        console.error("get event failed", error);
      });
  };

  useEffect(() => {
    fetchExam();

    fetch(`${BACKEND}/getyear`)
      .then((response) => response.json())
      .then((data) => setYear(data))
      .catch((error) => {
        console.error("get event failed", error);
      });

    fetch(`${BACKEND}/getmonth`)
      .then((response) => response.json())
      .then((data) => setMonth(data))
      .catch((error) => {
        console.error("get event failed", error);
      });
  }, []);

  return (
    <>
      <div>
        <h1>Admin Page</h1>
        <h2>Current Exam: {currentExam}</h2>
        <input
          type="text"
          placeholder="Enter Event ID"
          value={localExamName}
          onChange={(e) => setLocalExamName(e.target.value)}
        />
        <button onClick={changeExam}>Change Exam</button>
        <p></p>
        <p></p>
        <button onClick={refreshData}>Refresh Data</button>
        <p></p>
        <p></p>
        <p>Year: {year}</p>
        <p>Month: {month}</p>
      </div>
    </>
  );
};

export default Adminpage;
