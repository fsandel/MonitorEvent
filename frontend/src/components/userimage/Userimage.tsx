import React from "react";
import styled from "styled-components";

interface IUser {
  userName: string;
  userId: string;
  userImg?: string;
}

interface IUserentryProps {
  user: IUser;
}

const UserImageWrapper = styled.div`
  width: 300px; /* Default width for desktop */
  height: auto;

  @media (max-width: 768px) {
    width: 150px;
  }
`;

const ScaledImage = styled.img`
  width: 100%;
  height: auto;
`;

const Userimage: React.FC<IUserentryProps> = (props: IUserentryProps) => {
  return (
    <UserImageWrapper>
      <ScaledImage src={props.user.userImg} alt={props.user.userName} />
    </UserImageWrapper>
  );
};

export default Userimage;
