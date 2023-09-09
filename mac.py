import datetime
from sqlite3 import Timestamp
from time import sleep
import requests
import json


param = {
    #변경
        "addParam": "JTdCJTIyX3J1blBnbUtleSUyMjolMjJTRUxGX1NUVURTRUxGX1NVQl8zMFNFTEZfTUVOVV8xMFN1ZVJlcUxlc25FR3VpZGUlMjIsJTIyX3J1blN5c0tleSUyMjolMjJTQ0glMjIsJTIyX3J1bkludGdVc3JObyUyMjolMjIxOTAxMTU5NCUyMiwlMjJfcnVuUGdMb2dpbkR0JTIyOiUyMjIwMjIxMjAxMTE1ODUyJTIyLCUyMl9ydW5uaW5nU2Vqb25nJTIyOiUyMjU0N2MyNTJmLTU4ZTItNGQxOS05ZDZmLTIyNmZhNGZjM2U4MiUyMiU3RA=="
    }
url = 'https://sjpt.sejong.ac.kr/sch/sch/sue/SueReqLesnE/doInsert.do?'

def request1():
    ts = int(datetime.datetime.now().timestamp())
    #변경
    datas={"dm_search":{"KEY_ORGN_CLSF_CD":"20","KEY_YEAR":"2022","KEY_SMT_CD":"21","KEY_DEPT_CD":"","KEY_STUDENT_NO":"19011594","KEY_DAN_CD":"","KEY_MUST_L_CD":"","KEY_CURI_NM":"고전","KEY_CURI_NO":"","KEY_CLASS_NO":"","KEY_DIS_CDT":0,"KEY_DIS_CNT":0,"KEY_CORS_CD":"","KEY_SPECIAL_GET_CDT":"","KEY_YEAR_SMT_CD":"202221","KEY_SEARCH_DIV":"5","KEY_SEARCH_CORS_CD":"","KEY_SEARCH_ORGN_CLSF_CD":"20","KEY_SELF_CODE":"","STUDENT_DEPT_CD":"","STUDENT_YEAR":"","STUDENT_CLASS_CD":"","ROW_DEPT_CD":"9005","ROW_CURI_NO":"009780","ROW_CURI_NM":"고전특강","ROW_CLASS":"001","ROW_CURI_TYPE_CD":"12","ROW_ORGN_CLSF_CD":"20","ROW_DAN_CD":"","ROW_CORS_UNIT_GRP_CD":"","ROW_CDT":1,"ROW_CURI_DIV_CD":"1","ROW_CURI_TYPE_L_CD":"","ROW_MUST_L_CD":"","ROW_GRADE_TYPE_CD":"","ROW_STUDENT_YEAR":1,"ROW_FROM_STUDENT_YEAR":1,"ROW_TO_STUDENT_YEAR":5,"ROW_RE_YEAR":"","ROW_RE_SMT_CD":"","ROW_RE_ORGN_CLSF_CD":"","ROW_RE_CURI_NO":"","ROW_PREF_ORGN_CLSF_CD":"","ROW_PREF_CURI_NO":"","ROW_LESN_REQ_CD":"","ROW_TOT_LIMIT_RCNT":"","ROW_OUT_LIMIT_RCNT":"","ROW_CYBER_TYPE_CD":"","ROW_MASTER_THESIS_YN":"","ROW_DOCTOR_THESIS_YN":"","ROW_MASTER_INDEPENDENT_YN":"","ROW_DOCTOR_INDEPENDENT_YN":"","MY_ORGN_CLSF_CD":"20","MY_CORS_CD":"11","MY_DEPT_CD":"3215","MY_DAN_CD":"1","MY_NATION_CD":"","MY_STUDENT_YEAR":"4","MY_INOUT_MAIN_CD":"10","MY_INOUT_SUB_CD":"10","MY_ADMIT_SMT_CNT":"0","MY_EARLY_YN":"N","MY_MAJ_ING_YN":"N","MY_TEACHER_YN":"N","MY_VALID_SMT":7,"MY_CORS_SCHE_GRP_CD":"0","MY_CORS_UNIT_GRP_CD":"","MY_ENT_YEAR":"2019","MY_ENT_SMT_CD":"10","MY_RE_GDT_YEAR":"","USER_ERR_CODE":"0","MY_MAX_REQ_CDT":"6","KEY_PREF_CDT":"","KEY_KOR_CDT":"","KEY_STUDENT_NM":"이지호","MY_CURI_YEAR":"2019","MY_CURI_SMT_CD":"10","MY_MAJYEON_YN":"","MY_LESS_SMT_CNT":8,"MY_SCHO_CD":"","MY_COLL_DIV_CD":"10","MY_ETC_PART_CD":"","MY_SCH_REGI_CD":"11","MY_SCH_REGI_DT":"20190304","ROW_MY_SELF_DIV_CD":"SUE40","RETURN_CODE":"SUCCEED","MY_MAJ_BU_YN":"N","MY_MAJ_BOK_YN":"N","MY_MAJ_YEON_YN":"N","ROW_ENGLISH_YN":"N","ROW_CHAPEL_YN":"N","ROW_INTENSIVE_YN":"N","ROW_GDT_CURI_CD":"5","ROW_SEASON_CD":"1","NAV_INFO":"Netscape|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Safari/537.36|Mozilla|ko-KR|Win32|false","ROW_COLL_DIV_FOREIGNER_YN":"","ROW_COLL_DIV_LOCAL_YN":"","ROW_INTERNSHIP_TYPE_CD":"","MY_ROTC_YN":"","MY_ENG_LES_YN":"N"}}
    headers = {
        #변경
        "Host" : "sjpt.sejong.ac.kr",
        "Cookie" : f"WMONID=5u5ExcUhFnp; PO1_JSESSIONID=412a3d3db6f14fc5be704c1282d3c7b0420c8ecc84d2f96f39ff!-887189095!1669863511892; ROT_ROUTEID=.ROT_WAS41; SCH_ROUTEID=.SCH_WAS11; ssotoken=Vy3zFySFx5FWEBETCzTyGIDx5FSEJONGzCy1669864966zPy86400zAy34zEyUjE0UUYvFhRVFUlAdNx2BIbjQJekPx79x2FmU4r60O08fAYsw7b5sVfogPkPCGkhapcUqkn4njJh77gi1mX8x79pQhlx7A9FgOx2BIRfdlDVQvx789TABI7hqRLZDonkx2BTXjtGt4ukd6iLQFa80brKv6wAEeXux2FveZWLWlx2BPIqgms67gttx2F9x2BKgSDjEPv0MugM7x2FF49tuohhx798CRv6q347MASSrCvuADNsd8nR7gtQtO9M171ex79jCtx79gjx7ASUQkCx2FJI0jQBJIakC1DL7Q0VVG2Qx2Fm5TuquBkRr7qgjmEVOgwKEnOWMEaSKE4g13x2BRAmMfUERpjS5n7mkO04W5dMUfC4x79Lmlx2BRN0Yx79FDx2FH7X1Jx7AvdCfx2Fkx2FmiWkajx2FLjx79rWaSl9Jvx2BKm6x785x2Bx7ADah1DMsKOjBx2BQlBmoo9uUoKiEutX9ZBU6Qx78x2FaOx799mk9Bir1areEp8Kx2Fpk6IGitolx2Bj7GzKyux79evwMx7Ax2FTMex7A8oc1BFw7pdt8jXdEkx2FMHjvj87Lx2BjKFQx3DzSSy00001869061zUURy5b97af14d9ac76afzMynX4ItuGMgfsx3Dz; NetFunnel_ID=; NetFunnelID=; JSESSIONID=f826507d4290423e97c3d45486a9fd6446fbb88d0f853df36e86!1784183996; lastAccess={ts}",
        "Content-Length": "2356",
        "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"95\"",
        "Accept": "application/json",
        "Submissionid": "mf_tabMainCon_contents_SELF_STUDSELF_SUB_30SELF_MENU_10SueReqLesnEGuide_body_sub_insert",
        "Content-Type": "application/json; charset=\"UTF-8\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Origin": "https://sjpt.sejong.ac.kr",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://sjpt.sejong.ac.kr/main/view/Login/doSsoLogin.do?p=",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "close"
    }
    res = requests.post(url, params=param, headers=headers, data=json.dumps(datas))
    print(res.text, type(res))
    sleep(0.5)
    return res.text.find('과목이 신청 되었습니다. 수강신청내역을 재 조회 하시겠습니까?')

def request2():
    ts = int(datetime.datetime.now().timestamp())
    #변경
    datas={"dm_search":{"KEY_ORGN_CLSF_CD":"20","KEY_YEAR":"2022","KEY_SMT_CD":"21","KEY_DEPT_CD":"","KEY_STUDENT_NO":"19011594","KEY_DAN_CD":"","KEY_MUST_L_CD":"","KEY_CURI_NM":"고전","KEY_CURI_NO":"","KEY_CLASS_NO":"","KEY_DIS_CDT":0,"KEY_DIS_CNT":0,"KEY_CORS_CD":"","KEY_SPECIAL_GET_CDT":"","KEY_YEAR_SMT_CD":"202221","KEY_SEARCH_DIV":"5","KEY_SEARCH_CORS_CD":"","KEY_SEARCH_ORGN_CLSF_CD":"20","KEY_SELF_CODE":"","STUDENT_DEPT_CD":"","STUDENT_YEAR":"","STUDENT_CLASS_CD":"","ROW_DEPT_CD":"9005","ROW_CURI_NO":"009780","ROW_CURI_NM":"고전특강","ROW_CLASS":"002","ROW_CURI_TYPE_CD":"12","ROW_ORGN_CLSF_CD":"20","ROW_DAN_CD":"","ROW_CORS_UNIT_GRP_CD":"","ROW_CDT":1,"ROW_CURI_DIV_CD":"1","ROW_CURI_TYPE_L_CD":"","ROW_MUST_L_CD":"","ROW_GRADE_TYPE_CD":"","ROW_STUDENT_YEAR":1,"ROW_FROM_STUDENT_YEAR":1,"ROW_TO_STUDENT_YEAR":5,"ROW_RE_YEAR":"","ROW_RE_SMT_CD":"","ROW_RE_ORGN_CLSF_CD":"","ROW_RE_CURI_NO":"","ROW_PREF_ORGN_CLSF_CD":"","ROW_PREF_CURI_NO":"","ROW_LESN_REQ_CD":"","ROW_TOT_LIMIT_RCNT":"","ROW_OUT_LIMIT_RCNT":"","ROW_CYBER_TYPE_CD":"","ROW_MASTER_THESIS_YN":"","ROW_DOCTOR_THESIS_YN":"","ROW_MASTER_INDEPENDENT_YN":"","ROW_DOCTOR_INDEPENDENT_YN":"","MY_ORGN_CLSF_CD":"20","MY_CORS_CD":"11","MY_DEPT_CD":"3215","MY_DAN_CD":"1","MY_NATION_CD":"","MY_STUDENT_YEAR":"4","MY_INOUT_MAIN_CD":"10","MY_INOUT_SUB_CD":"10","MY_ADMIT_SMT_CNT":"0","MY_EARLY_YN":"N","MY_MAJ_ING_YN":"N","MY_TEACHER_YN":"N","MY_VALID_SMT":7,"MY_CORS_SCHE_GRP_CD":"0","MY_CORS_UNIT_GRP_CD":"","MY_ENT_YEAR":"2019","MY_ENT_SMT_CD":"10","MY_RE_GDT_YEAR":"","USER_ERR_CODE":"0","MY_MAX_REQ_CDT":"6","KEY_PREF_CDT":"","KEY_KOR_CDT":"","KEY_STUDENT_NM":"이지호","MY_CURI_YEAR":"2019","MY_CURI_SMT_CD":"10","MY_MAJYEON_YN":"","MY_LESS_SMT_CNT":8,"MY_SCHO_CD":"","MY_COLL_DIV_CD":"10","MY_ETC_PART_CD":"","MY_SCH_REGI_CD":"11","MY_SCH_REGI_DT":"20190304","ROW_MY_SELF_DIV_CD":"SUE40","RETURN_CODE":"SUCCEED","MY_MAJ_BU_YN":"N","MY_MAJ_BOK_YN":"N","MY_MAJ_YEON_YN":"N","ROW_ENGLISH_YN":"N","ROW_CHAPEL_YN":"N","ROW_INTENSIVE_YN":"N","ROW_GDT_CURI_CD":"5","ROW_SEASON_CD":"1","NAV_INFO":"Netscape|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Safari/537.36|Mozilla|ko-KR|Win32|false","ROW_COLL_DIV_FOREIGNER_YN":"","ROW_COLL_DIV_LOCAL_YN":"","ROW_INTERNSHIP_TYPE_CD":"","MY_ROTC_YN":"","MY_ENG_LES_YN":"N"}}
    headers = {
        #변경
        "Host" : "sjpt.sejong.ac.kr",
        "Cookie" : f"WMONID=5u5ExcUhFnp; PO1_JSESSIONID=412a3d3db6f14fc5be704c1282d3c7b0420c8ecc84d2f96f39ff!-887189095!1669863511892; ROT_ROUTEID=.ROT_WAS41; SCH_ROUTEID=.SCH_WAS11; ssotoken=Vy3zFySFx5FWEBETCzTyGIDx5FSEJONGzCy1669864966zPy86400zAy34zEyUjE0UUYvFhRVFUlAdNx2BIbjQJekPx79x2FmU4r60O08fAYsw7b5sVfogPkPCGkhapcUqkn4njJh77gi1mX8x79pQhlx7A9FgOx2BIRfdlDVQvx789TABI7hqRLZDonkx2BTXjtGt4ukd6iLQFa80brKv6wAEeXux2FveZWLWlx2BPIqgms67gttx2F9x2BKgSDjEPv0MugM7x2FF49tuohhx798CRv6q347MASSrCvuADNsd8nR7gtQtO9M171ex79jCtx79gjx7ASUQkCx2FJI0jQBJIakC1DL7Q0VVG2Qx2Fm5TuquBkRr7qgjmEVOgwKEnOWMEaSKE4g13x2BRAmMfUERpjS5n7mkO04W5dMUfC4x79Lmlx2BRN0Yx79FDx2FH7X1Jx7AvdCfx2Fkx2FmiWkajx2FLjx79rWaSl9Jvx2BKm6x785x2Bx7ADah1DMsKOjBx2BQlBmoo9uUoKiEutX9ZBU6Qx78x2FaOx799mk9Bir1areEp8Kx2Fpk6IGitolx2Bj7GzKyux79evwMx7Ax2FTMex7A8oc1BFw7pdt8jXdEkx2FMHjvj87Lx2BjKFQx3DzSSy00001869061zUURy5b97af14d9ac76afzMynX4ItuGMgfsx3Dz; NetFunnel_ID=; NetFunnelID=; JSESSIONID=f826507d4290423e97c3d45486a9fd6446fbb88d0f853df36e86!1784183996; lastAccess={ts}",
        "Content-Length": "2356",
        "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"95\"",
        "Accept": "application/json",
        "Submissionid": "mf_tabMainCon_contents_SELF_STUDSELF_SUB_30SELF_MENU_10SueReqLesnEGuide_body_sub_insert",
        "Content-Type": "application/json; charset=\"UTF-8\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Origin": "https://sjpt.sejong.ac.kr",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://sjpt.sejong.ac.kr/main/view/Login/doSsoLogin.do?p=",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "close"
    }
    res = requests.post(url, params=param, headers=headers, data=json.dumps(datas))
    print(res.text, type(res))
    sleep(0.5)
    return res.text.find('과목이 신청 되었습니다. 수강신청내역을 재 조회 하시겠습니까?')

def request3():
    ts = int(datetime.datetime.now().timestamp())
    #변경
    datas={"dm_search":{"KEY_ORGN_CLSF_CD":"20","KEY_YEAR":"2022","KEY_SMT_CD":"21","KEY_DEPT_CD":"","KEY_STUDENT_NO":"19011594","KEY_DAN_CD":"","KEY_MUST_L_CD":"","KEY_CURI_NM":"고전","KEY_CURI_NO":"","KEY_CLASS_NO":"","KEY_DIS_CDT":0,"KEY_DIS_CNT":0,"KEY_CORS_CD":"","KEY_SPECIAL_GET_CDT":"","KEY_YEAR_SMT_CD":"202221","KEY_SEARCH_DIV":"5","KEY_SEARCH_CORS_CD":"","KEY_SEARCH_ORGN_CLSF_CD":"20","KEY_SELF_CODE":"","STUDENT_DEPT_CD":"","STUDENT_YEAR":"","STUDENT_CLASS_CD":"","ROW_DEPT_CD":"9005","ROW_CURI_NO":"009780","ROW_CURI_NM":"고전특강","ROW_CLASS":"003","ROW_CURI_TYPE_CD":"12","ROW_ORGN_CLSF_CD":"20","ROW_DAN_CD":"","ROW_CORS_UNIT_GRP_CD":"","ROW_CDT":1,"ROW_CURI_DIV_CD":"1","ROW_CURI_TYPE_L_CD":"","ROW_MUST_L_CD":"","ROW_GRADE_TYPE_CD":"","ROW_STUDENT_YEAR":1,"ROW_FROM_STUDENT_YEAR":1,"ROW_TO_STUDENT_YEAR":5,"ROW_RE_YEAR":"","ROW_RE_SMT_CD":"","ROW_RE_ORGN_CLSF_CD":"","ROW_RE_CURI_NO":"","ROW_PREF_ORGN_CLSF_CD":"","ROW_PREF_CURI_NO":"","ROW_LESN_REQ_CD":"","ROW_TOT_LIMIT_RCNT":"","ROW_OUT_LIMIT_RCNT":"","ROW_CYBER_TYPE_CD":"","ROW_MASTER_THESIS_YN":"","ROW_DOCTOR_THESIS_YN":"","ROW_MASTER_INDEPENDENT_YN":"","ROW_DOCTOR_INDEPENDENT_YN":"","MY_ORGN_CLSF_CD":"20","MY_CORS_CD":"11","MY_DEPT_CD":"3215","MY_DAN_CD":"1","MY_NATION_CD":"","MY_STUDENT_YEAR":"4","MY_INOUT_MAIN_CD":"10","MY_INOUT_SUB_CD":"10","MY_ADMIT_SMT_CNT":"0","MY_EARLY_YN":"N","MY_MAJ_ING_YN":"N","MY_TEACHER_YN":"N","MY_VALID_SMT":7,"MY_CORS_SCHE_GRP_CD":"0","MY_CORS_UNIT_GRP_CD":"","MY_ENT_YEAR":"2019","MY_ENT_SMT_CD":"10","MY_RE_GDT_YEAR":"","USER_ERR_CODE":"0","MY_MAX_REQ_CDT":"6","KEY_PREF_CDT":"","KEY_KOR_CDT":"","KEY_STUDENT_NM":"이지호","MY_CURI_YEAR":"2019","MY_CURI_SMT_CD":"10","MY_MAJYEON_YN":"","MY_LESS_SMT_CNT":8,"MY_SCHO_CD":"","MY_COLL_DIV_CD":"10","MY_ETC_PART_CD":"","MY_SCH_REGI_CD":"11","MY_SCH_REGI_DT":"20190304","ROW_MY_SELF_DIV_CD":"SUE40","RETURN_CODE":"SUCCEED","MY_MAJ_BU_YN":"N","MY_MAJ_BOK_YN":"N","MY_MAJ_YEON_YN":"N","ROW_ENGLISH_YN":"N","ROW_CHAPEL_YN":"N","ROW_INTENSIVE_YN":"N","ROW_GDT_CURI_CD":"5","ROW_SEASON_CD":"1","NAV_INFO":"Netscape|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Safari/537.36|Mozilla|ko-KR|Win32|false","ROW_COLL_DIV_FOREIGNER_YN":"","ROW_COLL_DIV_LOCAL_YN":"","ROW_INTERNSHIP_TYPE_CD":"","MY_ROTC_YN":"","MY_ENG_LES_YN":"N"}}
    headers = {
        #변경
        "Host" : "sjpt.sejong.ac.kr",
        "Cookie" : f"WMONID=5u5ExcUhFnp; PO1_JSESSIONID=412a3d3db6f14fc5be704c1282d3c7b0420c8ecc84d2f96f39ff!-887189095!1669863511892; ROT_ROUTEID=.ROT_WAS41; SCH_ROUTEID=.SCH_WAS11; ssotoken=Vy3zFySFx5FWEBETCzTyGIDx5FSEJONGzCy1669864966zPy86400zAy34zEyUjE0UUYvFhRVFUlAdNx2BIbjQJekPx79x2FmU4r60O08fAYsw7b5sVfogPkPCGkhapcUqkn4njJh77gi1mX8x79pQhlx7A9FgOx2BIRfdlDVQvx789TABI7hqRLZDonkx2BTXjtGt4ukd6iLQFa80brKv6wAEeXux2FveZWLWlx2BPIqgms67gttx2F9x2BKgSDjEPv0MugM7x2FF49tuohhx798CRv6q347MASSrCvuADNsd8nR7gtQtO9M171ex79jCtx79gjx7ASUQkCx2FJI0jQBJIakC1DL7Q0VVG2Qx2Fm5TuquBkRr7qgjmEVOgwKEnOWMEaSKE4g13x2BRAmMfUERpjS5n7mkO04W5dMUfC4x79Lmlx2BRN0Yx79FDx2FH7X1Jx7AvdCfx2Fkx2FmiWkajx2FLjx79rWaSl9Jvx2BKm6x785x2Bx7ADah1DMsKOjBx2BQlBmoo9uUoKiEutX9ZBU6Qx78x2FaOx799mk9Bir1areEp8Kx2Fpk6IGitolx2Bj7GzKyux79evwMx7Ax2FTMex7A8oc1BFw7pdt8jXdEkx2FMHjvj87Lx2BjKFQx3DzSSy00001869061zUURy5b97af14d9ac76afzMynX4ItuGMgfsx3Dz; NetFunnel_ID=; NetFunnelID=; JSESSIONID=f826507d4290423e97c3d45486a9fd6446fbb88d0f853df36e86!1784183996; lastAccess={ts}",
        "Content-Length": "2356",
        "Sec-Ch-Ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"95\"",
        "Accept": "application/json",
        "Submissionid": "mf_tabMainCon_contents_SELF_STUDSELF_SUB_30SELF_MENU_10SueReqLesnEGuide_body_sub_insert",
        "Content-Type": "application/json; charset=\"UTF-8\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.107 Safari/537.36",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Origin": "https://sjpt.sejong.ac.kr",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://sjpt.sejong.ac.kr/main/view/Login/doSsoLogin.do?p=",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "close"
    }
    res = requests.post(url, params=param, headers=headers, data=json.dumps(datas))
    print(res.text, type(res))
    sleep(0.5)
    return res.text.find('과목이 신청 되었습니다. 수강신청내역을 재 조회 하시겠습니까?')



while(True):
    print("고전특강")
    ret1 = request1()
    print("고전특강2")
    ret2 = request2()
    print("고전특강3")
    ret3 = request3()
    
    #if(ret2 != -1):  # -1이면 못찾은거 
      #  break
