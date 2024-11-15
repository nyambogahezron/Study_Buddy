import Axios from '../utils/Axios';

type ApiCallProps = {
  url: string;
  method: 'get' | 'post' | 'put' | 'delete';
  body?: object;
};
export default async function ApiCall({ url, method, body }: ApiCallProps) {
  try {
    const response = await Axios[method](url, body);
    return response;
  } catch (error) {
    console.error(error);
    return null;
  }
}
