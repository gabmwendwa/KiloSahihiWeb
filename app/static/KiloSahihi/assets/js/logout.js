function logout() {
    if (localStorage.session_token) {
      localStorage.removeItem("session_token");
      location.assign("http://localhost:8002/login/");
    }
  }