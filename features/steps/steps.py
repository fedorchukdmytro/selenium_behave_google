from behave import *
from test import *


@given('a Google')
def step_iml(context):
    context.google = Google()

@when('open Google page')
def step_imp(context):
    context.google.open_site()

@when('check link {images}')
def check_link(context, images):
    context.google.check_link(images)




