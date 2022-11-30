export function setLocalStorageValue(key: string, value: any, ovveride: boolean = true): void {
    if (!ovveride && localStorage.getItem(key)) {
        throw 'Key alerdy exist';
    } 
    localStorage.setItem(key, value)
}

export function getLocalStorageValue(key: string, defaultValue: any = null): any {
    return localStorage.getItem(key) || defaultValue;
}