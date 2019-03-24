# -*- coding: utf-8 -*-


def test_auth_error(app):
    username = app.session.web_config['username']
    password = "qwerty"

    app.session.open_home_page()
    app.session.entry_to_email()

    app.session.input_username(username)
    app.session.input_password(password)

    element_text = app.session.get_element_text()

    assert element_text == "Неверный пароль"
