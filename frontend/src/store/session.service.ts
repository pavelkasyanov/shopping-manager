import axios from 'axios';
import * as store from './store';
import type { User } from '../models';
import { BACKEND_URL } from '../config';

import { setLocalStorageValue, getLocalStorageValue } from '../utils/locastorage'

export interface SessionState {
    loggedIn: boolean;
    message: string;
}


const emptySessionPayload: SessionState = {
    loggedIn: false,
    message: 'Not signed in',
};

let _isLoggedIn = false;
let sessionState: SessionState = emptySessionPayload;
export let accessToken: string;

const accessTokenLocalStorageKey = "accessToken";

export function isLoggedIn(): boolean {
    return getLocalStorageValue(accessTokenLocalStorageKey) !== null;
}

export function getAccessToken(): string {
    return getLocalStorageValue(accessTokenLocalStorageKey);
}

export async function login(username: string, password: string) {
    const message = `Signed in as ${username}`;
    const signinUrl = `${BACKEND_URL}/login/`;
    const body: Partial<User> = {
        username,
        password,
    };

    try {
        const response = await axios.post<{accessToken: string}>(signinUrl, body);
        let data = response.data;
        if (data?.accessToken) {
            accessToken = data.accessToken;
            sessionState = { loggedIn: true, message };
            store.getSession(sessionState);
            setLocalStorageValue(accessTokenLocalStorageKey, accessToken);
            return true;
        } else {
            logout();
            return false;
        } 
    } catch(error) {
        logout();
        return false;
    }
}

export function logout() {
    accessToken = null;
    _isLoggedIn = false;
    sessionState = emptySessionPayload;
    store.getSession(sessionState);
}

