# Task 5 - Test your Dash application
# Test suite to varify dash application is working as expected
from dash.testing.application_runners import import_app


# Test to check whether header for dash application is present or not
def test_bsly001_check_header(dash_duo):
    app = import_app("task_6_test_automation.dash_app_visualization")
    dash_duo.start_server(app)
    # assert len(dash_duo.find_elements("#header")) == 1, "Dash application's header is not present"
    dash_duo.wait_for_element("#header", timeout=4), "Dash application's header is not present"


# Test to check whether chart to visualize Pink Morsel's sales data is present or not
def test_bsly002_check_visualization(dash_duo):
    app = import_app("task_6_test_automation.dash_app_visualization")
    dash_duo.start_server(app)
    # assert len(dash_duo.find_elements("#graph-with-radio-button")) == 1, "Chart to visualize Pink Morsel's sales data is not present in your Dash application"
    dash_duo.wait_for_element("#graph-with-radio-button",
                              timeout=4), "Chart to visualize Pink Morsel's sales data is not present in your Dash application"


# Test to check whether Pink Morsel's sales region picker is present or not
def test_bsly003_check_region_picker(dash_duo):
    app = import_app("task_6_test_automation.dash_app_visualization")
    dash_duo.start_server(app)
    # assert len(dash_duo.find_elements("#sales-region-picker")) == 1, "Sales region picker to visualize region wise sales is not present in your Dash application"
    dash_duo.wait_for_element("#sales-region-picker",
                              timeout=4), "Sales region picker to visualize region wise sales is not present in your Dash application"
