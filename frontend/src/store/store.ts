import { writable, type Writable } from 'svelte/store';
import type { SessionState } from './session.service';

const emptySessionPayload: SessionState = {
    loggedIn: false,
    message: 'Not signed in',
};

interface AppState {
    session: Writable<SessionState>;
}

const state: AppState = {
    session: writable(emptySessionPayload),
}

const getSession = (session: SessionState) => {
    state.session.update((old: SessionState) => session);
};

export {
    state,
    getSession,
  };