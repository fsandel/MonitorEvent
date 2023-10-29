import { useParams } from "react-router-dom";
import Userpage from "../components/userpage";

const User: React.FC = () => {
  const { userIdParam } = useParams();
  let userId = userIdParam;
  if (userId === undefined) userId = "";

  return (
    <>
      <Userpage />
    </>
  );
};

export default User;
