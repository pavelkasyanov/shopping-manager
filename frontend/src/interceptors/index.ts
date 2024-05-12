import { authInterceptor } from './auth.interceptor';

export function applyHttpInterceptors() {
    
    const interceptors = [
        /**
        * Auth:
        *    Add the authentication headers.
        */
        authInterceptor,
    ]

    interceptors.reverse().forEach((f) => f());
}