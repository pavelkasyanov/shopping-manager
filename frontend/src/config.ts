// const API: string = process.env.SVELTE_APP_API || 'api';
// const DEV: boolean = !!process.env.DEV || true;

const BACKEND_URL: string = 'http://localhost:8000';
const API_URL: string = BACKEND_URL + '/api/v1';
const DEV: boolean = true;

function logRouteLocation(location: Object) {
    console.log(DEV);
}
  
export { BACKEND_URL, API_URL, DEV, logRouteLocation };
