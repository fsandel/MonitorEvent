import React, { useEffect, useState } from "react";
import { BACKEND } from "../../types/constants";
import { IPVersion } from "net";

interface IEvent {
  eventName: string;
  eventDescription: string;
  eventSubscriber: string;
}

const emptyEvent: IEvent = {
  eventName: "name",
  eventDescription: "description",
  eventSubscriber: "subs",
};

const EventComponent: React.FC = () => {
  const [currentEvent, setCurrentEvent] = useState(emptyEvent);

  useEffect(() => {
    fetch(`${BACKEND}/geteventinformation`)
      .then((response) => response.json())
      .then((data: IEvent) => setCurrentEvent(data))
      .catch((error) => {
        console.error("get event failed", error);
      });
  }, []);

  return (
    <>
      <div>
        <h2>{currentEvent.eventName}</h2>
        <p>{currentEvent.eventDescription}</p>
        <p>with {currentEvent.eventSubscriber} subscribers</p>
      </div>
    </>
  );
};

export default EventComponent;
