import React, { useState } from "react";

const Adminpage: React.FC = () => {
  const [eventId, setEventId] = useState("");

  const handlePostRequest = () => {
    fetch("http://localhost:4000/event", {
      method: "POST",
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
        <button onClick={handlePostRequest}>Post Request</button>
      </div>
    </>
  );
};

export default Adminpage;
