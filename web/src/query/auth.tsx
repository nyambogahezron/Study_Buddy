import Axios from '../utils/Axios';

type RegisterUserProps = {
  email: string;
  name: string;
  username: string;
  password: string;
};
// Register a new user
export default async function RegisterUser({
  email,
  password,
  name,
  username,
}: RegisterUserProps) {
  try {
    const response = await Axios.post('/register/', {
      email,
      password,
      name,
      username,
    });
    return response;
  } catch (error) {
    console.error(error);
    return null;
  }
}

//Login a user
export async function LoginUser({
  email,
  password,
}: {
  email: string;
  password: string;
}) {
  try {
    const response = await Axios.post('/login/', {
      email,
      password,
    });
    return response;
  } catch (error) {
    console.error(error);
    return null;
  }
}

//Logout a user
export async function LogoutUser() {
  try {
    const response = await Axios.post('/logout/');
    return response;
  } catch (error) {
    console.error(error);
    return null;
  }
}
