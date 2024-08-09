import streamlit as st
import streamlit_authenticator as stauth
import yaml  # type: ignore
from yaml.loader import SafeLoader  # type: ignore


class FixedAuthenticate(stauth.Authenticate):
    """A temporary fix which allows `Authenticate` to log out properly."""

    # TODO: Install the latest version to fix the bug. https://github.com/mkhorasani/Streamlit-Authenticator/issues/134
    def _implement_logout(self):
        # Clears cookie and session state variables associated with the logged-in user.
        try:
            self.cookie_manager.delete(self.cookie_name)
        except Exception as exc:
            print(exc)
        self.credentials["usernames"][st.session_state["username"]]["logged_in"] = False
        st.session_state["logout"] = True
        st.session_state["name"] = None
        st.session_state["username"] = None
        st.session_state["authentication_status"] = None


################################################################################
# Streamlit app
################################################################################

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

st.set_page_config(page_title="Email Generation PoC", layout="centered")
authenticator = FixedAuthenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["preauthorized"],
)
name, authentication_status, username = authenticator.login()

if st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")
elif st.session_state["authentication_status"]:
    authenticator.logout()

    welcome_subscriber_email = st.Page(
        "templates/welcome_subscriber.py",
        title="Generate welcome subscriber email",
        icon=":material/add_circle:",
    )

    pg = st.navigation([welcome_subscriber_email])
    pg.run()
