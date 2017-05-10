# -*- coding: utf-8 -*-
from data.for_contact_form import testdata
import pytest

@pytest.mark.usefixtures()
@pytest.mark.parametrize("personal_info", testdata)
def test_test_contact_us(app, personal_info):
    app.open_home_page()
    app.open_how_we_can_help_you()
    app.open_request_consultation()
    app.fill_request_consultation_form1()
    app.fill_consultation_form2(personal_info)
    app.submit_request_consultation_form()
