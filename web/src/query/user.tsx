import Axios from '../utils/Axios';

//Get the current user
export async function GetCurrentUser() {
  try {
    const response = await Axios.get('/auth/me');
    return response;
  } catch (error) {
    console.error(error);
    return null;
  }
}

//Update the current user
export async function UpdateCurrentUser({
  email,
  name,
  username,
}: {
  email: string;
  name: string;
  username: string;
}) {
  try {
    const response = await Axios.put('/auth/me', {
      email,
      name,
      username,
    });
    return response;
  } catch (error) {
    console.error(error);
    return null;
  }
}

//Update the current user password
export async function UpdateCurrentUserPassword({
  password,
}: {
  password: string;
}) {
  try {
    const response = await Axios.put('/auth/me/password', {
      password,
    });
    return response;
  } catch (error) {
    console.error(error);
    return null;
  }
}

//Delete the current user
export async function DeleteCurrentUser() {
  try {
    const response = await Axios.delete('/auth/me');
    return response;
  } catch (error) {
    console.error(error);
    return null;
  }
}

//Get all users
export async function GetAllUsers() {
  try {
    const response = await Axios.get('/users');
    return response;
  } catch (error) {
    console.error(error);
    return null;
  }
}

//Get a user by id
export async function GetUserById(id: string) {
  try {
    const response = await Axios.get(`/users/${id}`);
    return response;
  } catch (error) {
    console.error(error);
    return null;
  }
}
