import React, { useState } from "react";

const Adminpage: React.FC = () => {
  const [eventId, setEventId] = useState("");

  const handlePostEvent = () => {
    fetch("http://localhost:4000/event", {
      method: "POST",
      mode: "no-cors", // Set the mode to "no-cors"
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
    fetch("http://localhost:4000/setup", {
      method: "POST",
      mode: "no-cors", // Set the mode to "no-cors"
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

  return (
    <>
      <div>
        <h1>Admin Page</h1>
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
