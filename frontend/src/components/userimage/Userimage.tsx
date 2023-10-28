import React from "react";

interface IUser {
  userName: string;
  userId: string;
  userImg?: string;
}

interface IUserentryProps {
  user: IUser;
}

const Userimage: React.FC<IUserentryProps> = (props: IUserentryProps) => {
  return (
    <>
      <img src={props.user.userImg}></img>
    </>
  );
};

export default Userimage;
