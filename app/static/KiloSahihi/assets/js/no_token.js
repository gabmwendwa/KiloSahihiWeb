// localStorage.removeItem("session_token");
if (!localStorage.session_token) {
    if(!localStorage.last_location)
      localStorage.setItem("last_location", location.href);
  
    location.assign(applink+"login/");
}