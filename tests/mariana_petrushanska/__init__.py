# def test_all_characters(group_of_characters, test_password):
#     errors = []
#     for value in group_of_characters:
#         final_password = test_password + value
#         result = check_password(final_password)
#         if result is False:
#             errors.append(value)
#     assert len(errors) == 0, f"There is an error for {errors} character(s), which cannot be used in password, but should."
