import type { AxiosError, AxiosRequestConfig, AxiosResponse } from 'axios';
import { logErrorMessage } from './log';

export const prefixReq = '⬇ -';
export const prefixRes = '⬆ -';

export interface AxiosMeta {
  started?: number;
}

export interface AxiosRequestConfigExtended extends AxiosRequestConfig {
  meta: AxiosMeta;
}

export interface AxiosResponseExtended extends AxiosResponse {
  config: AxiosRequestConfigExtended;
}

export function logError(error: AxiosError) {
  const msg =
    error.config && error.response
      ? `Http Response Error for ${error?.config?.url}\nreturned with status ${error?.response?.status}\n${error}`
      : error;

  logErrorMessage(`${prefixRes} 🛑 Log Http Response Error`, [msg]);
}