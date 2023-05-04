from behave import when, given, then
from time import sleep

@given('Open cureskin shop page')
def open_cureskin_shop(context):
    context.app.shop_page.open_main()
    sleep(5)

@when('close popup')
def close_popup(context):
    context.app.shop_page.close_popup()


@when('enter invalid email {email}')
def input_invalid_email(context, email):
    context.app.footer_page.input_email_text(email)
    context.app.footer_page.submit_email()
    sleep(2)


@when('enter valid email {email}')
def input_valid_email(context, email):
    context.app.footer_page.clear_email_field()
    context.app.footer_page.input_email_text(email)
    context.app.footer_page.submit_email()
    sleep(5)


@then('verify that {text}')
def verify_email_worked(context, text):
    context.app.footer_page.verify_email_confirmation(text)
