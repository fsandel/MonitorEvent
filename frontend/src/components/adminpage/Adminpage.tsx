import React, { useEffect, useState } from "react";
import { BACKEND } from "../../types/constants";

const Adminpage: React.FC = () => {
  const [eventId, setEventId] = useState("");
  const [currentEventId, setCurrentEventId] = useState("");

  const handlePostEvent = () => {
    fetch(`${BACKEND}/event`, {
      method: "POST",
      mode: "no-cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ eventId }),
    })
      .then((response) => {
        console.log("POST request successful");
      })
      .catch((error) => {
        console.error("Error making POST request:", error);
      });
  };

  const handlePostSetup = () => {
    fetch(`${BACKEND}/setup`, {
      method: "POST",
      mode: "no-cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ eventId }),
    })
      .then((response) => {
        console.log("POST request successful");
      })
      .catch((error) => {
        console.error("Error making POST request:", error);
      });
  };

  useEffect(() => {
    fetch(`${BACKEND}/geteventid`, {
      // mode: "no-cors",
      // headers: {
      //   "Content-Type": "application/json",
      // },
    })
      .then((response) => response.json())
      .then((data) => setCurrentEventId(data))
      .catch((error) => {
        console.error("get event failed", error);
      });
  }, []);

  return (
    <>
      <div>
        <h1>Admin Page</h1>
        <h2>Current EventId: {currentEventId}</h2>
        <input
          type="text"
          placeholder="Enter Event ID"
          value={eventId}
          onChange={(e) => setEventId(e.target.value)}
        />
        <button onClick={handlePostEvent}>Post Request</button>
        <p></p>
        <p></p>
        <button onClick={handlePostSetup}>Refresh Data</button>
      </div>
    </>
  );
};

export default Adminpage;
