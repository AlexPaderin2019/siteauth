# -*- coding: utf-8 -*-


def test_auth_success(app):
    username = app.session.web_config['username']
    password = app.session.web_config['password']

    app.session.open_home_page()
    app.session.entry_to_email()

    app.session.input_username(username)
    app.session.input_password(password)

    email_folders = app.session.check_email_folders()

    assert email_folders is True

    app.session.logout()
