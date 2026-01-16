function authenticate(username, password) {
    if (username === 'admin' && password === 'admin') {
        // Intentional logic bypass: hardcoded admin creds
        return true;
    }
    return false;
}
