# from behave import *
# import requests
# from api_payload import *
#
#
# @given('the book details which needs to be added to Library')
# def steps_implimentation(context):
#     add_book = response.json()
#     print(add_book).
#     add_book_id = add_book["ID"]
#     print("Book ID: ", add_book_id)
#
#
# @when(u'we execute the AddBook PostAPI method')
# def step_impl(context):
#     add_url = get_config()['API']['endpoint'] + resources.add_book
#     response = requests.post(add_url, json=add_book_payload("240501"),
#                              headers={"Content-Type": "application/json; charset=UTF-8"}, )
#
#
# @then(u'book successfully added')
# def step_impl(context):
#     add_book = response.json()
#     print(add_book)
#     add_book_id = add_book["ID"]
#     print("Book ID: ", add_book_id)
#
