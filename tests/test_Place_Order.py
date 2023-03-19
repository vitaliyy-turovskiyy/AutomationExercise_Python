import pytest


from pages.Place_Order_Page import OrderPage
from playwright.sync_api import expect
from data.test_data import Data
from pages.Signup_Login_Page import SignupPage
from utils.tools import take_screenshot


class TestContactUs:

    @pytest.fixture
    def test_setup(self, page):
        self.page = page
        self.page.set_viewport_size(viewport_size={ 'width': 1366, 'height': 768 })
        self.order = OrderPage(self.page)
        self.signup = SignupPage(self.page)
        self.page.goto('http://automationexercise.com')

    def test_TestCase14_Place_Order_Register_while_Checkout(self, page, test_setup):
        self.order.add_to_card1_click()
        self.order.view_cart_btn_click()
        expect(page).to_have_url('https://automationexercise.com/view_cart')

        self.order.check_out_btn_click()
        self.order.register_login_btn_click()

        self.signup.name_input(Data.name)
        self.signup.email_signup_input(Data.email)
        self.signup.signup_btn_click()
        self.signup.check_enter_account_information_lbl()
        self.signup.title_mr_click()
        self.signup.password_field_input(Data.password)
        self.signup.day_of_birth_click()
        self.signup.newsletter_checkbox_click()
        self.signup.first_name_input(Data.firstname)
        self.signup.last_name_field_input(Data.lastname)
        self.signup.company_field_input(Data.company)
        self.signup.address1_field_input(Data.address)
        self.signup.address2_field_input(Data.address2)
        self.signup.state_field_input(Data.state)
        self.signup.city_field_input(Data.city)
        self.signup.zipcode_field_input(Data.zipcode)
        self.signup.mobile_number_field_input(Data.mobilenumber)
        self.signup.create_account_btn_click()

        self.signup.account_created_lbl_check()
        self.signup.continue_btn_click()

        self.signup.logged_in_as_user_lbl_check()
        self.order.view_cart_button_click()
        self.order.check_out_btn_click()
        expect(self.order.address_delivery_field).to_contain_text("New street,2")
        self.order.form_control_field_fill()
        self.order.place_order_btn_click()

        self.order.name_on_card_fill(Data.NameonCard)
        self.order.card_number_fill(Data.CardNumber)
        self.order.cvc_number_fill(Data.CVC)
        self.order.expiry_month_fill(Data.Expiration)
        self.order.expiry_year_fill(Data.date)
        self.order.pay_button_click()

        self.order.check_success_message()

        self.signup.delete_account_btn_click()
        self.signup.delete_account_lbl_check()
        self.signup.continue_btn2_click()
        take_screenshot(self.page, "Place_Order_Register_while_Checkout")

    def test_TestCase15_Place_Order_Register_before_Checkout(self, page, test_setup):
        self.signup.signup_login_btn_click()
        self.signup.name_input(Data.name)
        self.signup.email_signup_input(Data.email)
        self.signup.signup_btn_click()
        self.signup.check_enter_account_information_lbl()
        self.signup.title_mr_click()
        self.signup.password_field_input(Data.password)
        self.signup.day_of_birth_click()
        self.signup.newsletter_checkbox_click()
        self.signup.first_name_input(Data.firstname)
        self.signup.last_name_field_input(Data.lastname)
        self.signup.company_field_input(Data.company)
        self.signup.address1_field_input(Data.address)
        self.signup.address2_field_input(Data.address2)
        self.signup.state_field_input(Data.state)
        self.signup.city_field_input(Data.city)
        self.signup.zipcode_field_input(Data.zipcode)
        self.signup.mobile_number_field_input(Data.mobilenumber)
        self.signup.create_account_btn_click()

        self.signup.account_created_lbl_check()
        self.signup.continue_btn_click()

        self.signup.logged_in_as_user_lbl_check()

        self.order.add_to_card1_click()
        self.order.view_cart_btn_click()
        expect(page).to_have_url('https://automationexercise.com/view_cart')
        self.order.check_out_btn_click()
        expect(self.order.address_delivery_field).to_contain_text("New street,2")
        self.order.form_control_field_fill()
        self.order.place_order_btn_click()

        self.order.name_on_card_fill(Data.NameonCard)
        self.order.card_number_fill(Data.CardNumber)
        self.order.cvc_number_fill(Data.CVC)
        self.order.expiry_month_fill(Data.Expiration)
        self.order.expiry_year_fill(Data.date)
        self.order.pay_button_click()

        self.order.check_success_message()

        self.signup.delete_account_btn_click()
        self.signup.delete_account_lbl_check()
        self.signup.continue_btn2_click()
        take_screenshot(self.page, "Place_Order_Register_before_Checkout")

    def test_TestCase16_Login_before_Checkout(self, page, test_setup):
        self.signup.signup_login_btn_click()
        self.signup.login_email_address_field_input(Data.email2)
        self.signup.login_password_field_input(Data.password)
        self.signup.login_btn_click()

        self.order.add_to_card1_click()
        self.order.view_cart_btn_click()
        expect(page).to_have_url('https://automationexercise.com/view_cart')
        self.order.check_out_btn_click()
        expect(self.order.address_delivery_field).to_contain_text("New street,2")
        self.order.form_control_field_fill()
        self.order.place_order_btn_click()

        self.order.name_on_card_fill(Data.NameonCard)
        self.order.card_number_fill(Data.CardNumber)
        self.order.cvc_number_fill(Data.CVC)
        self.order.expiry_month_fill(Data.Expiration)
        self.order.expiry_year_fill(Data.date)
        self.order.pay_button_click()

        self.order.check_success_message()

        self.signup.delete_account_btn_click()
        self.signup.delete_account_lbl_check()
        self.signup.continue_btn2_click()
        take_screenshot(self.page, "Login_before_Checkout")

    def test_TestCase23_Verify_address_details_in_checkout_page(self, page, test_setup):
        self.signup.signup_login_btn_click()
        self.signup.name_input(Data.name)
        self.signup.email_signup_input(Data.email)
        self.signup.signup_btn_click()
        self.signup.check_enter_account_information_lbl()
        self.signup.title_mr_click()
        self.signup.password_field_input(Data.password)
        self.signup.day_of_birth_click()
        self.signup.newsletter_checkbox_click()
        self.signup.first_name_input(Data.firstname)
        self.signup.last_name_field_input(Data.lastname)
        self.signup.company_field_input(Data.company)
        self.signup.address1_field_input(Data.address)
        self.signup.address2_field_input(Data.address2)
        self.signup.state_field_input(Data.state)
        self.signup.city_field_input(Data.city)
        self.signup.zipcode_field_input(Data.zipcode)
        self.signup.mobile_number_field_input(Data.mobilenumber)
        self.signup.create_account_btn_click()

        self.signup.account_created_lbl_check()
        self.signup.continue_btn_click()

        self.signup.logged_in_as_user_lbl_check()

        self.order.add_to_card1_click()
        self.order.view_cart_btn_click()
        expect(page).to_have_url('https://automationexercise.com/view_cart')
        self.order.check_out_btn_click()
        expect(self.order.address_delivery_field).to_contain_text("New street,2")
        expect(self.order.address_billing_field).to_contain_text("New street,22")
        self.signup.delete_account_btn_click()
        self.signup.delete_account_lbl_check()
        self.signup.continue_btn2_click()
        take_screenshot(self.page, "Verify_address_details_in_checkout_page")

    def test_TestCase24_Download_Invoice_after_purchase_order(self, page, test_setup):
        self.order.add_to_card1_click()
        self.order.view_cart_btn_click()
        expect(page).to_have_url('https://automationexercise.com/view_cart')
        self.order.check_out_btn_click()

        self.signup.register_login_click()
        self.signup.name_input(Data.name)
        self.signup.email_signup_input(Data.email)
        self.signup.signup_btn_click()
        self.signup.check_enter_account_information_lbl()
        self.signup.title_mr_click()
        self.signup.password_field_input(Data.password)
        self.signup.day_of_birth_click()
        self.signup.newsletter_checkbox_click()
        self.signup.first_name_input(Data.firstname)
        self.signup.last_name_field_input(Data.lastname)
        self.signup.company_field_input(Data.company)
        self.signup.address1_field_input(Data.address)
        self.signup.address2_field_input(Data.address2)
        self.signup.state_field_input(Data.state)
        self.signup.city_field_input(Data.city)
        self.signup.zipcode_field_input(Data.zipcode)
        self.signup.mobile_number_field_input(Data.mobilenumber)
        self.signup.create_account_btn_click()

        self.signup.account_created_lbl_check()
        self.signup.continue_btn_click()

        self.signup.logged_in_as_user_lbl_check()
        self.order.view_cart_button_click()
        self.order.check_out_btn_click()
        expect(self.order.address_delivery_field).to_contain_text("New street,2")
        self.order.form_control_field_fill()
        self.order.place_order_btn_click()

        self.order.name_on_card_fill(Data.NameonCard)
        self.order.card_number_fill(Data.CardNumber)
        self.order.cvc_number_fill(Data.CVC)
        self.order.expiry_month_fill(Data.Expiration)
        self.order.expiry_year_fill(Data.date)
        self.order.pay_button_click()

        self.order.check_success_message()
        self.order.download_invoice_btn_click()

        self.signup.continue_btn2_click()
        self.signup.delete_account_btn_click()
        self.signup.delete_account_lbl_check()
        take_screenshot(self.page, "Download_Invoice_after_purchase_order")

















