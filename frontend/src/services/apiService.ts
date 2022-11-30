import axios from 'axios';
import { API_URL } from '../config';

export async function getAllUsers(): Promise<any> {
    const url = `${API_URL}/users/all`;
    const response = await axios.get(url, {headers: {'Content-Type': 'application/json'}, data: {}});
    return response?.data;
}