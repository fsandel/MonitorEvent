import React from "react";

interface IUser {
  userName: string;
  userId: string;
}

interface IUserentryProps {
  user: IUser;
}

const Userentry: React.FC<IUserentryProps> = (props: IUserentryProps) => {
  return (
    <>
      <p>{props.user.userName}</p>
    </>
  );
};

export default Userentry;
