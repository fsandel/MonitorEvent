import React, { useEffect, useState } from "react";
import { BACKEND } from "../../types/constants";
import EventComponent from "../event/Event";

const Adminpage: React.FC = () => {
  const [eventId, setEventId] = useState("");
  const [currentEventId, setCurrentEventId] = useState("");
  const [eventComponentKey, setEventComponentKey] = useState(0);

  const changeEvent = () => {
    fetch(`${BACKEND}/event`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ eventId }),
    })
      .then((response) => {
        console.log("POST request successful");
        // Update the key to trigger re-render of EventComponent
        setEventComponentKey((prevKey) => prevKey + 1);
      })
      .catch((error) => {
        console.error("Error making POST request:", error);
      });
  };

  const handlePostSetup = () => {
    fetch(`${BACKEND}/setup`, {
      method: "POST",
      headers: {
        "Content-Type": "application json",
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

  const fetchEventId = () => {
    fetch(`${BACKEND}/geteventid`)
      .then((response) => response.json())
      .then((data) => setCurrentEventId(data))
      .catch((error) => {
        console.error("get event failed", error);
      });
  };

  useEffect(() => {
    fetchEventId();
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
        <button onClick={changeEvent}>Change Event</button>
        <p></p>
        <p></p>
        <button onClick={handlePostSetup}>Refresh Data</button>
        <p></p>
        <p></p>
        <EventComponent key={eventComponentKey} />
      </div>
    </>
  );
};

export default Adminpage;
