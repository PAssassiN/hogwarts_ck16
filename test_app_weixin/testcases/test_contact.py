from test_app_weixin.page.app import App


def test_add_member():
    app = App()
    app.start()
    res = app.goto_main().goto_address().click_add_member().add_member_manual().add_contact()
    assert res is True
