import { navigate } from 'svelte-routing';
import axios, {
    type AxiosError,
    type AxiosRequestConfig,
    type AxiosResponse,
} from 'axios';
import { prefixReq } from './../utils/http-config';
import { logMessage } from './../utils/log';
import * as sessionService from '../store/session.service';



export function authInterceptor() {
    axios.interceptors.request.use((config: AxiosRequestConfig) => {
        const { accessToken } = sessionService;
        
        if (accessToken) {
            config.headers.Authorization = `Bearer ${accessToken}`;
            config.withCredentials = true;
            logMessage(`${prefixReq} 🔑 Auth`, [`Adding Auth header`]);
        } else {
            logMessage(`${prefixReq} 🔑 Auth`, [`No Auth Token to add`]);
        }

        return config;
    });

    
    axios.interceptors.response.use(
        (response: AxiosResponse) => response,
        (error: AxiosError) => {
            if (error.response.status === 401) {
                if(error.response.data) {
                    navigate('/login');
                } else {
                }
                return Promise.resolve(true);
            }
            return Promise.reject(error);
        },
    );
}