import React from "react";
import Userimage from "../userimage";
import styled from "styled-components";

interface IUser {
  userName: string;
  userId: string;
  userImg?: string;
  registered: boolean;
}

interface IUserentryProps {
  user: IUser;
}

const UserentryWrapper = styled.div`
  display: flex;
  align-items: center;
`;

const UserContainer = styled.div`
  display: flex;
  align-items: center;
  border: 1px solid black;
  padding: 10px; /* Add padding to create whitespace */
`;

const UserName = styled.div`
  flex: 3;
  margin-left: 10px;
`;

const Userentry: React.FC<IUserentryProps> = (props: IUserentryProps) => {
  return (
    <UserentryWrapper>
      <UserContainer>
        <Userimage user={props.user} />
        <UserName>
          <div>
            <p>{props.user.userName}</p>
            <p>{props.user.registered}</p>
          </div>
        </UserName>
      </UserContainer>
    </UserentryWrapper>
  );
};

export default Userentry;
