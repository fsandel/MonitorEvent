import React from "react";

const Userlist: React.FC = () => {
  fetch("http://localhost:4000/raw")
    .then((res) => res.json())
    .then((data) => console.log(data))
    .catch(() => console.log("error"));
  return (
    <>
      <p>userlist</p>
    </>
  );
};

export default Userlist;
