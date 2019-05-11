# -*- coding: utf-8 -*-

from authentication.authentication import getJWTToken
from models import Member, Events, Gallery, ProfilePictures, Account, \
    EventAttendees, GalleryPictures
from tnaapp.helper_functions import JSONResponse

data = {
    "tnaapp.member": [{
        "google": None,
        "ev_token": None,
        "last_name": "",
        "post_type": "ME",
        "tw_url": "",
        "first_name": "TNA",
        "date_of_birth": None,
        "ln_url": "",
        "is_verified": False,
        "email": "turkunepal@gmail.com",
        "is_active": True,
        "pr_token": None,
        "phone": "",
        "is_admin": True,
        "is_board_member": False,
        "address": "",
        "post": None,
        "password": "pbkdf2_sha256$20000$fv967Jho6BO4$HoC59qBMDXVOp7lx9aObuMCd+A8aYtdwgOdW9D20HYE=",
        "skype": "",
        "github": "",
        "fb_url": "",
        "url": "",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOiIiLCJldl90b2tlbiI6bnVsbCwibGFzdF9uYW1lIjoiIiwicG9zdF90eXBlIjoiTUUiLCJza3lwZSI6IiIsImZpcnN0X25hbWUiOiJUTkEiLCJkYXRlX29mX2JpcnRoIjpudWxsLCJsYXN0X2xvZ2luIjoiMjAxNy0wOS0wOFQyMTo0NzoyNi40NDIiLCJwayI6MSwibG5fdXJsIjoiIiwiaXNfdmVyaWZpZWQiOmZhbHNlLCJlbWFpbCI6InR1cmt1bmVwYWxAZ21haWwuY29tIiwiaXNfYWN0aXZlIjp0cnVlLCJwcl90b2tlbiI6bnVsbCwicGhvbmUiOiIiLCJpc19hZG1pbiI6dHJ1ZSwiaXNfYm9hcmRfbWVtYmVyIjpmYWxzZSwiYWRkcmVzcyI6IiIsInBvc3QiOm51bGwsInBhc3N3b3JkIjoicGJrZGYyX3NoYTI1NiQyMDAwMCRmdjk2N0pobzZCTzQkSG9DNTlxQk1EWFZPcDdseDlhT2J1TUNkK0E4YVl0ZHdnT2RXOUQyMEhZRT0iLCJnaXRodWIiOiIiLCJmYl91cmwiOiIiLCJ1cmwiOiIiLCJ0d191cmwiOiIifQ.xSpK0WdMlG4keSumsAItXrgZYunxMkws8ASc9JeIzLE",
        "pk": 1
    }, {
        "google": None,
        "ev_token": None,
        "last_name": "Karki",
        "post_type": "BM",
        "tw_url": "",
        "first_name": "Sudhir",
        "date_of_birth": None,
        "ln_url": "",
        "is_verified": True,
        "email": "friendlysudhir@yahoo.com",
        "is_active": True,
        "pr_token": None,
        "phone": "",
        "is_admin": False,
        "is_board_member": True,
        "address": "",
        "post": "CM",
        "password": "pbkdf2_sha256$20000$B9KgUFoGy71c$3p84XFJrNFowR8Afj18/PPey2Jts/1lmevQF2iCvLvA=",
        "skype": "",
        "github": "",
        "fb_url": "",
        "url": "",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOiIiLCJldl90b2tlbiI6bnVsbCwibGFzdF9uYW1lIjoiS2Fya2kiLCJwb3N0X3R5cGUiOiJCTSIsInNreXBlIjoiIiwiZmlyc3RfbmFtZSI6IlN1ZGhpciIsImRhdGVfb2ZfYmlydGgiOm51bGwsImxhc3RfbG9naW4iOiIyMDE2LTEwLTA0VDE5OjUwOjQ5Ljc2MiIsInBrIjoyLCJsbl91cmwiOiIiLCJpc192ZXJpZmllZCI6dHJ1ZSwiZW1haWwiOiJmcmllbmRseXN1ZGhpckB5YWhvby5jb20iLCJpc19hY3RpdmUiOnRydWUsInByX3Rva2VuIjpudWxsLCJwaG9uZSI6IiIsImlzX2FkbWluIjpmYWxzZSwiaXNfYm9hcmRfbWVtYmVyIjp0cnVlLCJhZGRyZXNzIjoiIiwicG9zdCI6IkNNIiwicGFzc3dvcmQiOiJwYmtkZjJfc2hhMjU2JDIwMDAwJEI5S2dVRm9HeTcxYyQzcDg0WEZKck5Gb3dSOEFmajE4L1BQZXkySnRzLzFsbWV2UUYyaUN2THZBPSIsImdpdGh1YiI6IiIsImZiX3VybCI6IiIsInVybCI6IiIsInR3X3VybCI6IiJ9.lQX_yTaCU4nkhJmilrRPZ8BS8HbOZ-aNjKKt0nIITWg",
        "pk": 2
    }, {
        "google": "",
        "ev_token": "",
        "last_name": "Bashyal",
        "post_type": "ME",
        "tw_url": "",
        "first_name": "Barun",
        "date_of_birth": None,
        "ln_url": "",
        "is_verified": False,
        "email": "barun@smartmobe.fi",
        "is_active": True,
        "pr_token": "",
        "phone": "",
        "is_admin": False,
        "is_board_member": False,
        "address": "",
        "post": None,
        "password": "sfsdfsafsf",
        "skype": "",
        "github": "",
        "fb_url": "",
        "url": "",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOiIiLCJldl90b2tlbiI6bnVsbCwibGFzdF9uYW1lIjoiQmFzaHlhbCIsInBvc3RfdHlwZSI6Ik1FIiwic2t5cGUiOiIiLCJmaXJzdF9uYW1lIjoiQmFydW4iLCJkYXRlX29mX2JpcnRoIjpudWxsLCJsYXN0X2xvZ2luIjoiMjAxNi0xMC0xMVQxOToyNToxOS4yNTIiLCJwayI6MywibG5fdXJsIjoiIiwiaXNfdmVyaWZpZWQiOmZhbHNlLCJlbWFpbCI6ImJhcnVuQHNtYXJ0bW9iZS5maSIsImlzX2FjdGl2ZSI6dHJ1ZSwicHJfdG9rZW4iOiIiLCJwaG9uZSI6IiIsImlzX2FkbWluIjpmYWxzZSwiaXNfYm9hcmRfbWVtYmVyIjp0cnVlLCJhZGRyZXNzIjoiIiwicG9zdCI6bnVsbCwicGFzc3dvcmQiOiJwYmtkZjJfc2hhMjU2JDIwMDAwJERGSzRRSk1GM2RSdCQyVDNYTVZFMGdXcThhS1llM0FrMUdYeHZFTUg2SlNUUHFiQnNTUTdMMmdVPSIsImdpdGh1YiI6IiIsImZiX3VybCI6IiIsInVybCI6IiIsInR3X3VybCI6IiJ9.RQJc1p3nmQHxJ_HbWLCW6bCR_Vv69pDVKUqvBNc9DKQ",
        "pk": 3
    }, {
        "google": None,
        "ev_token": None,
        "last_name": "Mahat",
        "post_type": "BM",
        "tw_url": "",
        "first_name": "Hari Krishna",
        "date_of_birth": "1970-01-01",
        "ln_url": "",
        "is_verified": True,
        "email": "hmahat@gmail.com",
        "is_active": True,
        "pr_token": "",
        "phone": "0449882332",
        "is_admin": False,
        "is_board_member": True,
        "address": "Turku",
        "post": "SE",
        "password": "pbkdf2_sha256$20000$sbTyzh3501Zl$HD4fwLaG5Ly1ewZKbuCw3T951aAkI0h0N1kjB2QrXDk=",
        "skype": "",
        "github": "",
        "fb_url": "http://facebook.com/mahathari",
        "url": "",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaWVsZHMiOnsiZ29vZ2xlIjpudWxsLCJldl90b2tlbiI6bnVsbCwibGFzdF9uYW1lIjoiTWFoYXQiLCJwb3N0X3R5cGUiOiJCTSIsInNreXBlIjoiIiwiZmlyc3RfbmFtZSI6IkhhcmkgS3Jpc2huYSIsImRhdGVfb2ZfYmlydGgiOiIxOTcwLTAxLTAxIiwibG5fdXJsIjoiIiwiaXNfdmVyaWZpZWQiOnRydWUsImVtYWlsIjoiaG1haGF0QGdtYWlsLmNvbSIsImlzX2FjdGl2ZSI6dHJ1ZSwicHJfdG9rZW4iOiIiLCJwaG9uZSI6IjA0NDk4ODIzMzIiLCJpc19hZG1pbiI6ZmFsc2UsImlzX2JvYXJkX21lbWJlciI6dHJ1ZSwiYWRkcmVzcyI6IlR1cmt1IiwicG9zdCI6IlNFIiwicGFzc3dvcmQiOiJwYmtkZjJfc2hhMjU2JDIwMDAwJHNiVHl6aDM1MDFabCRIRDRmd0xhRzVMeTFld1pLYnVDdzNUOTUxYUFrSTBoME4xa2pCMlFyWERrPSIsImdpdGh1YiI6IiIsImZiX3VybCI6Imh0dHA6Ly9mYWNlYm9vay5jb20vbWFoYXRoYXJpIiwidXJsIjoiIiwidHdfdXJsIjoiIn0sIm1vZGVsIjoidG5hYXBwLm1lbWJlciIsInBrIjo0fQ.vqZNkmQEag7rtd0XCeVdRW5hJXhtJuwvPqRb6-biYVs",
        "pk": 4
    }, {
        "google": "",
        "ev_token": "",
        "last_name": "Lama",
        "post_type": "ME",
        "tw_url": "",
        "first_name": "Rakesh Tamang",
        "date_of_birth": None,
        "ln_url": "",
        "is_verified": False,
        "email": "lama.rakes@gmail.com",
        "is_active": True,
        "pr_token": "",
        "phone": "",
        "is_admin": False,
        "is_board_member": False,
        "address": "",
        "post": None,
        "password": "25873e159d36d8c7218c74bbfd3d7e02",
        "skype": "",
        "github": "",
        "fb_url": "",
        "url": "",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOiIiLCJldl90b2tlbiI6bnVsbCwibGFzdF9uYW1lIjoiTGFtYSIsInBvc3RfdHlwZSI6Ik1FIiwic2t5cGUiOiIiLCJmaXJzdF9uYW1lIjoiUmFrZXNoIFRhbWFuZyIsImRhdGVfb2ZfYmlydGgiOm51bGwsImxhc3RfbG9naW4iOm51bGwsInBrIjo1LCJsbl91cmwiOiIiLCJpc192ZXJpZmllZCI6ZmFsc2UsImVtYWlsIjoibGFtYS5yYWtlc0BnbWFpbC5jb20iLCJpc19hY3RpdmUiOnRydWUsInByX3Rva2VuIjpudWxsLCJwaG9uZSI6IiIsImlzX2FkbWluIjpmYWxzZSwiaXNfYm9hcmRfbWVtYmVyIjp0cnVlLCJhZGRyZXNzIjoiIiwicG9zdCI6bnVsbCwicGFzc3dvcmQiOiIyNTg3M2UxNTlkMzZkOGM3MjE4Yzc0YmJmZDNkN2UwMiIsImdpdGh1YiI6IiIsImZiX3VybCI6IiIsInVybCI6IiIsInR3X3VybCI6IiJ9.KxxZJWVO6J-STG5CRrBp6gjjUtfPJZA053mSEn1cm34",
        "pk": 5
    }, {
        "google": None,
        "ev_token": None,
        "last_name": "Yadav",
        "post_type": "BM",
        "tw_url": "",
        "first_name": "Aman",
        "date_of_birth": "1989-01-28",
        "ln_url": "https://www.linkedin.com/in/amanpdyadav",
        "is_verified": True,
        "email": "amanpdyadav@gmail.com",
        "is_active": True,
        "pr_token": "",
        "phone": "(+358) 044 021 0054",
        "is_admin": False,
        "is_board_member": True,
        "address": "Yo-Kylä 5D 14",
        "post": "DO",
        "password": "pbkdf2_sha256$20000$zKcszxY8LZkZ$p9fKIzeXWvc6alT+LWrSr0TCAU4A4BWET6qOpD2+4GY=",
        "skype": "aman.yadav30",
        "github": "https://github.com/amanpdyadav",
        "fb_url": "https://www.facebook.com/amanpdyadav",
        "url": "https://amanyadav.net/",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaWVsZHMiOnsiZ29vZ2xlIjpudWxsLCJldl90b2tlbiI6bnVsbCwibGFzdF9uYW1lIjoiWWFkYXYiLCJwb3N0X3R5cGUiOiJCTSIsInNreXBlIjoiYW1hbi55YWRhdjMwIiwiZmlyc3RfbmFtZSI6IkFtYW4iLCJkYXRlX29mX2JpcnRoIjoiMTk4OS0wMS0yOCIsImxuX3VybCI6Imh0dHBzOi8vd3d3LmxpbmtlZGluLmNvbS9pbi9hbWFucGR5YWRhdiIsImlzX3ZlcmlmaWVkIjp0cnVlLCJlbWFpbCI6ImFtYW5wZHlhZGF2QGdtYWlsLmNvbSIsImlzX2FjdGl2ZSI6dHJ1ZSwicHJfdG9rZW4iOiIiLCJwaG9uZSI6IigrMzU4KSAwNDQgMDIxIDAwNTQiLCJpc19hZG1pbiI6ZmFsc2UsImlzX2JvYXJkX21lbWJlciI6dHJ1ZSwiYWRkcmVzcyI6IllvLUt5bFx1MDBlNCA1RCAxNCIsInBvc3QiOiJETyIsInBhc3N3b3JkIjoicGJrZGYyX3NoYTI1NiQyMDAwMCR6S2NzenhZOExaa1okcDlmS0l6ZVhXdmM2YWxUK0xXclNyMFRDQVU0QTRCV0VUNnFPcEQyKzRHWT0iLCJnaXRodWIiOiJodHRwczovL2dpdGh1Yi5jb20vYW1hbnBkeWFkYXYiLCJmYl91cmwiOiJodHRwczovL3d3dy5mYWNlYm9vay5jb20vYW1hbnBkeWFkYXYiLCJ1cmwiOiJodHRwczovL2FtYW55YWRhdi5uZXQvIiwidHdfdXJsIjoiIn0sIm1vZGVsIjoidG5hYXBwLm1lbWJlciIsInBrIjo2fQ.YB2fwimnH_ZA6JIY8DLtvIOiVT2IEP6CsDAsaizG7h4",
        "pk": 6
    }, {
        "google": None,
        "ev_token": "",
        "last_name": None,
        "post_type": "ME",
        "tw_url": None,
        "first_name": "Kalyan giri",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "kalyangiri@hotmail.com",
        "is_active": True,
        "pr_token": None,
        "phone": None,
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$BK1eNQlDYkql$zwxQUgFJf/jjgqlwUAewFvDVC/QNlOh0BO+TUp9yAI8=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOm51bGwsImV2X3Rva2VuIjoiIiwibGFzdF9uYW1lIjpudWxsLCJwb3N0X3R5cGUiOiJNRSIsInNreXBlIjpudWxsLCJmaXJzdF9uYW1lIjoiS2FseWFuIGdpcmkiLCJkYXRlX29mX2JpcnRoIjpudWxsLCJsYXN0X2xvZ2luIjoiMjAxNi0xMC0xNlQxMzoyMDowNy43MTUiLCJwayI6NywibG5fdXJsIjpudWxsLCJpc192ZXJpZmllZCI6ZmFsc2UsImVtYWlsIjoia2FseWFuZ2lyaUBob3RtYWlsLmNvbSIsImlzX2FjdGl2ZSI6dHJ1ZSwicHJfdG9rZW4iOm51bGwsInBob25lIjpudWxsLCJpc19hZG1pbiI6ZmFsc2UsImlzX2JvYXJkX21lbWJlciI6ZmFsc2UsImFkZHJlc3MiOm51bGwsInBvc3QiOm51bGwsInBhc3N3b3JkIjoicGJrZGYyX3NoYTI1NiQyMDAwMCRCSzFlTlFsRFlrcWwkend4UVVnRkpmL2pqZ3Fsd1VBZXdGdkRWQy9RTmxPaDBCTytUVXA5eUFJOD0iLCJnaXRodWIiOm51bGwsImZiX3VybCI6bnVsbCwidXJsIjpudWxsLCJ0d191cmwiOm51bGx9.3OSp3aWiDexd_DKlcglrUrdZFfKM73dcDfN5AGZHBa4",
        "pk": 7
    }, {
        "google": None,
        "ev_token": "",
        "last_name": None,
        "post_type": "ME",
        "tw_url": None,
        "first_name": "Chandra",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "visitchandra122@gmail.com",
        "is_active": True,
        "pr_token": "",
        "phone": None,
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$8R6wRJV5p7rY$7nTqklG6Gq8VuuwDSevjx3k/tlQKZY7bVXnGSb9jYLM=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOm51bGwsImV2X3Rva2VuIjoiIiwibGFzdF9uYW1lIjpudWxsLCJwb3N0X3R5cGUiOiJNRSIsInNreXBlIjpudWxsLCJmaXJzdF9uYW1lIjoiQ2hhbmRyYSIsImRhdGVfb2ZfYmlydGgiOm51bGwsImxhc3RfbG9naW4iOiIyMDE2LTEwLTExVDE5OjE4OjMyLjM3MCIsInBrIjo4LCJsbl91cmwiOm51bGwsImlzX3ZlcmlmaWVkIjpmYWxzZSwiZW1haWwiOiJ2aXNpdGNoYW5kcmExMjJAZ21haWwuY29tIiwiaXNfYWN0aXZlIjp0cnVlLCJwcl90b2tlbiI6IiIsInBob25lIjpudWxsLCJpc19hZG1pbiI6ZmFsc2UsImlzX2JvYXJkX21lbWJlciI6ZmFsc2UsImFkZHJlc3MiOm51bGwsInBvc3QiOm51bGwsInBhc3N3b3JkIjoicGJrZGYyX3NoYTI1NiQyMDAwMCQ4UjZ3UkpWNXA3clkkN25UcWtsRzZHcThWdXV3RFNldmp4M2svdGxRS1pZN2JWWG5HU2I5allMTT0iLCJnaXRodWIiOm51bGwsImZiX3VybCI6bnVsbCwidXJsIjpudWxsLCJ0d191cmwiOm51bGx9.TkLT_bBBdxLP1S4ILjdi3-J3FnTFu78PDz7nDxwPXqE",
        "pk": 8
    }, {
        "google": None,
        "ev_token": "",
        "last_name": "Kanth",
        "post_type": "ME",
        "tw_url": None,
        "first_name": "Rajeev Kanth",
        "date_of_birth": "1971-07-29",
        "ln_url": "",
        "is_verified": True,
        "email": "rajeevkanth7@gmail.com",
        "is_active": True,
        "pr_token": None,
        "phone": "00358440210074",
        "is_admin": False,
        "is_board_member": False,
        "address": "Kraatarinknatu 3 D 34",
        "post": None,
        "password": "pbkdf2_sha256$20000$QbAwOiy8oeoK$vKJB4R0sdRkg+QNyswExY/+5vlqqYqs211Ot7dQu0mI=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaWVsZHMiOnsiZ29vZ2xlIjpudWxsLCJldl90b2tlbiI6IiIsImxhc3RfbmFtZSI6IkthbnRoIiwicG9zdF90eXBlIjoiTUUiLCJza3lwZSI6bnVsbCwiZmlyc3RfbmFtZSI6IlJhamVldiBLYW50aCIsImRhdGVfb2ZfYmlydGgiOiIxOTcxLTA3LTI5IiwibG5fdXJsIjoiIiwiaXNfdmVyaWZpZWQiOnRydWUsImVtYWlsIjoicmFqZWV2a2FudGg3QGdtYWlsLmNvbSIsImlzX2FjdGl2ZSI6dHJ1ZSwicHJfdG9rZW4iOm51bGwsInBob25lIjoiMDAzNTg0NDAyMTAwNzQiLCJpc19hZG1pbiI6ZmFsc2UsImlzX2JvYXJkX21lbWJlciI6ZmFsc2UsImFkZHJlc3MiOiJLcmFhdGFyaW5rbmF0dSAzIEQgMzQiLCJwb3N0IjpudWxsLCJwYXNzd29yZCI6InBia2RmMl9zaGEyNTYkMjAwMDAkUWJBd09peThvZW9LJHZLSkI0UjBzZFJrZytRTnlzd0V4WS8rNXZscXFZcXMyMTFPdDdkUXUwbUk9IiwiZ2l0aHViIjpudWxsLCJmYl91cmwiOm51bGwsInVybCI6bnVsbCwidHdfdXJsIjpudWxsfSwibW9kZWwiOiJ0bmFhcHAubWVtYmVyIiwicGsiOjl9.gqgfJnDSJpoAAfv0cZ5K0BOvR4a2Y0ohH6hr4sC1lIg",
        "pk": 9
    }, {
        "google": None,
        "ev_token": "",
        "last_name": None,
        "post_type": "ME",
        "tw_url": None,
        "first_name": "Prajil Limbu",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "limbuprajil@yahoo.com",
        "is_active": True,
        "pr_token": None,
        "phone": None,
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$VCxyTs2ZLhYE$L+yJ1Zz4gcSZGlRRBBwEYX2B8GEvGBFvnCRP3cfljGU=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOm51bGwsImV2X3Rva2VuIjoiIiwibGFzdF9uYW1lIjpudWxsLCJwb3N0X3R5cGUiOiJNRSIsInNreXBlIjpudWxsLCJmaXJzdF9uYW1lIjoiUHJhamlsIExpbWJ1IiwiZGF0ZV9vZl9iaXJ0aCI6bnVsbCwibGFzdF9sb2dpbiI6IjIwMTYtMDktMjBUMTY6MjI6NTkuMzMwIiwicGsiOjEyLCJsbl91cmwiOm51bGwsImlzX3ZlcmlmaWVkIjpmYWxzZSwiZW1haWwiOiJsaW1idXByYWppbEB5YWhvby5jb20iLCJpc19hY3RpdmUiOnRydWUsInByX3Rva2VuIjpudWxsLCJwaG9uZSI6bnVsbCwiaXNfYWRtaW4iOmZhbHNlLCJpc19ib2FyZF9tZW1iZXIiOmZhbHNlLCJhZGRyZXNzIjpudWxsLCJwb3N0IjpudWxsLCJwYXNzd29yZCI6InBia2RmMl9zaGEyNTYkMjAwMDAkVkN4eVRzMlpMaFlFJEwreUoxWno0Z2NTWkdsUlJCQndFWVgyQjhHRXZHQkZ2bkNSUDNjZmxqR1U9IiwiZ2l0aHViIjpudWxsLCJmYl91cmwiOm51bGwsInVybCI6bnVsbCwidHdfdXJsIjpudWxsfQ.7uoa8i7l3qH6AIZVhY75mx33zW_r_vguZZupqOt6tOc",
        "pk": 12
    }, {
        "google": None,
        "ev_token": "",
        "last_name": None,
        "post_type": "ME",
        "tw_url": None,
        "first_name": "Bibek Acharya",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "bibwt@yahoo.com",
        "is_active": True,
        "pr_token": None,
        "phone": None,
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$O8PHFiegm25C$etys1k3o/xwJ6ACx7OkT9/cCXEqj39BCQvwNcHSBCHA=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOm51bGwsImV2X3Rva2VuIjoiIiwibGFzdF9uYW1lIjpudWxsLCJwb3N0X3R5cGUiOiJNRSIsInNreXBlIjpudWxsLCJmaXJzdF9uYW1lIjoiQmliZWsgQWNoYXJ5YSIsImRhdGVfb2ZfYmlydGgiOm51bGwsImxhc3RfbG9naW4iOiIyMDE2LTEwLTAyVDE4OjM1OjM0LjEwOSIsInBrIjoxMywibG5fdXJsIjpudWxsLCJpc192ZXJpZmllZCI6ZmFsc2UsImVtYWlsIjoiYmlid3RAeWFob28uY29tIiwiaXNfYWN0aXZlIjp0cnVlLCJwcl90b2tlbiI6bnVsbCwicGhvbmUiOm51bGwsImlzX2FkbWluIjpmYWxzZSwiaXNfYm9hcmRfbWVtYmVyIjpmYWxzZSwiYWRkcmVzcyI6bnVsbCwicG9zdCI6bnVsbCwicGFzc3dvcmQiOiJwYmtkZjJfc2hhMjU2JDIwMDAwJE84UEhGaWVnbTI1QyRldHlzMWszby94d0o2QUN4N09rVDkvY0NYRXFqMzlCQ1F2d05jSFNCQ0hBPSIsImdpdGh1YiI6bnVsbCwiZmJfdXJsIjpudWxsLCJ1cmwiOm51bGwsInR3X3VybCI6bnVsbH0.qkrH2kddJg2s-3UNNumCOoZtdS60K0AnPyNK2CpAS-s",
        "pk": 13
    }, {
        "google": None,
        "ev_token": "",
        "last_name": None,
        "post_type": "ME",
        "tw_url": None,
        "first_name": "Narayan Prasad Pokhrel",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "narayan.pokhrel8@gmail.com",
        "is_active": True,
        "pr_token": "",
        "phone": None,
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$bmw5taEMtzhh$CJbA+3mEX2YKlv3OJGc2q3nNupVGZ5J5kaV674umsgY=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOm51bGwsImV2X3Rva2VuIjoiIiwibGFzdF9uYW1lIjpudWxsLCJwb3N0X3R5cGUiOiJNRSIsInNreXBlIjpudWxsLCJmaXJzdF9uYW1lIjoiTmFyYXlhbiBQcmFzYWQgUG9raHJlbCIsImRhdGVfb2ZfYmlydGgiOm51bGwsImxhc3RfbG9naW4iOiIyMDE2LTEwLTI3VDAxOjQ0OjIxLjAyOSIsInBrIjoxNCwibG5fdXJsIjpudWxsLCJpc192ZXJpZmllZCI6ZmFsc2UsImVtYWlsIjoibmFyYXlhbi5wb2tocmVsOEBnbWFpbC5jb20iLCJpc19hY3RpdmUiOnRydWUsInByX3Rva2VuIjoiIiwicGhvbmUiOm51bGwsImlzX2FkbWluIjpmYWxzZSwiaXNfYm9hcmRfbWVtYmVyIjpmYWxzZSwiYWRkcmVzcyI6bnVsbCwicG9zdCI6bnVsbCwicGFzc3dvcmQiOiJwYmtkZjJfc2hhMjU2JDIwMDAwJGJtdzV0YUVNdHpoaCRDSmJBKzNtRVgyWUtsdjNPSkdjMnEzbk51cFZHWjVKNWthVjY3NHVtc2dZPSIsImdpdGh1YiI6bnVsbCwiZmJfdXJsIjpudWxsLCJ1cmwiOm51bGwsInR3X3VybCI6bnVsbH0.lEeEwL_6pepmi55XbHVSt01WOnEZyp0d4ARRAK1eKlI",
        "pk": 14
    }, {
        "google": None,
        "ev_token": "",
        "last_name": None,
        "post_type": "ME",
        "tw_url": None,
        "first_name": "Bikram pangeni",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "bikrampangeni85@gmail.com",
        "is_active": True,
        "pr_token": None,
        "phone": None,
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$zSy9r2qlI8jU$iNdSZRoNNcVVJ3J6wS4kdWuCICFrBhcJt2RPEo2S72o=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaWVsZHMiOnsiZ29vZ2xlIjpudWxsLCJldl90b2tlbiI6IiIsImxhc3RfbmFtZSI6bnVsbCwicG9zdF90eXBlIjoiTUUiLCJza3lwZSI6bnVsbCwiZmlyc3RfbmFtZSI6IkJpa3JhbSBwYW5nZW5pIiwiZGF0ZV9vZl9iaXJ0aCI6bnVsbCwibG5fdXJsIjpudWxsLCJpc192ZXJpZmllZCI6ZmFsc2UsImVtYWlsIjoiYmlrcmFtcGFuZ2VuaTg1QGdtYWlsLmNvbSIsImlzX2FjdGl2ZSI6dHJ1ZSwicHJfdG9rZW4iOm51bGwsInBob25lIjpudWxsLCJpc19hZG1pbiI6ZmFsc2UsImlzX2JvYXJkX21lbWJlciI6ZmFsc2UsImFkZHJlc3MiOm51bGwsInBvc3QiOm51bGwsInBhc3N3b3JkIjoicGJrZGYyX3NoYTI1NiQyMDAwMCR6U3k5cjJxbEk4alUkaU5kU1pSb05OY1ZWSjNKNndTNGtkV3VDSUNGckJoY0p0MlJQRW8yUzcybz0iLCJnaXRodWIiOm51bGwsImZiX3VybCI6bnVsbCwidXJsIjpudWxsLCJ0d191cmwiOm51bGx9LCJtb2RlbCI6InRuYWFwcC5tZW1iZXIiLCJwayI6MTV9.4oYRdo5vSxvsI4KxYLKTC8NydMEskO0OmBLNgLvVX-Q",
        "pk": 15
    }, {
        "google": None,
        "ev_token": "",
        "last_name": None,
        "post_type": "ME",
        "tw_url": None,
        "first_name": "sanjib gurung",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "gurung.sanjib@gmail.com",
        "is_active": True,
        "pr_token": None,
        "phone": None,
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$nB1mOHy52QM1$DybWEIJIwlKPstxtzLbBfve5Vg9XotIQfzDbvF7qAkc=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOm51bGwsImV2X3Rva2VuIjoiIiwibGFzdF9uYW1lIjpudWxsLCJwb3N0X3R5cGUiOiJNRSIsInNreXBlIjpudWxsLCJmaXJzdF9uYW1lIjoic2FuamliIGd1cnVuZyIsImRhdGVfb2ZfYmlydGgiOm51bGwsImxhc3RfbG9naW4iOiIyMDE3LTA1LTMwVDIyOjA4OjI0Ljk0NiIsInBrIjoxNiwibG5fdXJsIjpudWxsLCJpc192ZXJpZmllZCI6ZmFsc2UsImVtYWlsIjoiZ3VydW5nLnNhbmppYkBnbWFpbC5jb20iLCJpc19hY3RpdmUiOnRydWUsInByX3Rva2VuIjpudWxsLCJwaG9uZSI6bnVsbCwiaXNfYWRtaW4iOmZhbHNlLCJpc19ib2FyZF9tZW1iZXIiOmZhbHNlLCJhZGRyZXNzIjpudWxsLCJwb3N0IjpudWxsLCJwYXNzd29yZCI6InBia2RmMl9zaGEyNTYkMjAwMDAkbkIxbU9IeTUyUU0xJER5YldFSUpJd2xLUHN0eHR6TGJCZnZlNVZnOVhvdElRZnpEYnZGN3FBa2M9IiwiZ2l0aHViIjpudWxsLCJmYl91cmwiOm51bGwsInVybCI6bnVsbCwidHdfdXJsIjpudWxsfQ.j3ZTSCcN_N95t77fkdhz36HU-uqiFHYBz1Nobbrt2ys",
        "pk": 16
    }, {
        "google": None,
        "ev_token": "a7011ac458fabf7f0132c65a",
        "last_name": None,
        "post_type": "ME",
        "tw_url": None,
        "first_name": "Ajit Bahadur thapa",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "magarajit330@gmail.com",
        "is_active": False,
        "pr_token": None,
        "phone": None,
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$wW1vE6iVgiga$noc3kBV1BnaqaJ/LqA6LTqeIvkwjhxKYTw+cXJnHgfE=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOm51bGwsImV2X3Rva2VuIjoiYTcwMTFhYzQ1OGZhYmY3ZjAxMzJjNjVhIiwibGFzdF9uYW1lIjpudWxsLCJwb3N0X3R5cGUiOiJNRSIsInNreXBlIjpudWxsLCJmaXJzdF9uYW1lIjoiQWppdCBCYWhhZHVyIHRoYXBhIiwiZGF0ZV9vZl9iaXJ0aCI6bnVsbCwibGFzdF9sb2dpbiI6IjIwMTYtMTAtMDRUMjI6MzQ6MDAuNTMxIiwicGsiOjE3LCJsbl91cmwiOm51bGwsImlzX3ZlcmlmaWVkIjpmYWxzZSwiZW1haWwiOiJtYWdhcmFqaXQzMzBAZ21haWwuY29tIiwiaXNfYWN0aXZlIjpmYWxzZSwicHJfdG9rZW4iOm51bGwsInBob25lIjpudWxsLCJpc19hZG1pbiI6ZmFsc2UsImlzX2JvYXJkX21lbWJlciI6ZmFsc2UsImFkZHJlc3MiOm51bGwsInBvc3QiOm51bGwsInBhc3N3b3JkIjoicGJrZGYyX3NoYTI1NiQyMDAwMCR3VzF2RTZpVmdpZ2Ekbm9jM2tCVjFCbmFxYUovTHFBNkxUcWVJdmt3amh4S1lUdytjWEpuSGdmRT0iLCJnaXRodWIiOm51bGwsImZiX3VybCI6bnVsbCwidXJsIjpudWxsLCJ0d191cmwiOm51bGx9.PF9RvIyI8vNcNg_hDKR2ULq6gdNDZ8OGlMjDPeUASAU",
        "pk": 17
    }, {
        "google": None,
        "ev_token": "",
        "last_name": "Bahadur Baral(Roshan)",
        "post_type": "ME",
        "tw_url": None,
        "first_name": "Purna",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "sanusarlahi@gmail.com",
        "is_active": True,
        "pr_token": None,
        "phone": "0442369743",
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$Bu8YaE0eduks$xvvJia0L5WmWqYvQkEkd7aSKb9snWgbinlKQc4/N9E4=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOm51bGwsImV2X3Rva2VuIjoiIiwibGFzdF9uYW1lIjoiQmFoYWR1ciBCYXJhbChSb3NoYW4pIiwicG9zdF90eXBlIjoiTUUiLCJza3lwZSI6bnVsbCwiZmlyc3RfbmFtZSI6IlB1cm5hIiwiZGF0ZV9vZl9iaXJ0aCI6bnVsbCwibGFzdF9sb2dpbiI6IjIwMTYtMTItMTlUMDI6MzI6NTUuNDY3IiwicGsiOjE4LCJsbl91cmwiOm51bGwsImlzX3ZlcmlmaWVkIjpmYWxzZSwiZW1haWwiOiJzYW51c2FybGFoaUBnbWFpbC5jb20iLCJpc19hY3RpdmUiOnRydWUsInByX3Rva2VuIjpudWxsLCJwaG9uZSI6IjA0NDIzNjk3NDMiLCJpc19hZG1pbiI6ZmFsc2UsImlzX2JvYXJkX21lbWJlciI6ZmFsc2UsImFkZHJlc3MiOm51bGwsInBvc3QiOm51bGwsInBhc3N3b3JkIjoicGJrZGYyX3NoYTI1NiQyMDAwMCRCdThZYUUwZWR1a3MkeHZ2SmlhMEw1V21XcVl2UWtFa2Q3YVNLYjlzbldnYmlubEtRYzQvTjlFND0iLCJnaXRodWIiOm51bGwsImZiX3VybCI6bnVsbCwidXJsIjpudWxsLCJ0d191cmwiOm51bGx9.RRkM7ocUHzK4PdxxXGAH3XoNBFHNW7ZkJn1-q8QXwQ8",
        "pk": 18
    }, {
        "google": None,
        "ev_token": "164afb0181ce334041154354",
        "last_name": None,
        "post_type": "ME",
        "tw_url": None,
        "first_name": "sanjog raj shrestha",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "sanjogstha7@gmail.com",
        "is_active": False,
        "pr_token": None,
        "phone": None,
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$3xAT8x1nCGJ5$o0mRPK8tyf7R34gqARtOWFG4iFXcd9O2bZYvLfL/AW4=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOm51bGwsImV2X3Rva2VuIjoiMTY0YWZiMDE4MWNlMzM0MDQxMTU0MzU0IiwibGFzdF9uYW1lIjpudWxsLCJwb3N0X3R5cGUiOiJNRSIsInNreXBlIjpudWxsLCJmaXJzdF9uYW1lIjoic2Fuam9nIHJhaiBzaHJlc3RoYSIsImRhdGVfb2ZfYmlydGgiOm51bGwsImxhc3RfbG9naW4iOiIyMDE2LTEwLTI2VDIwOjQzOjQwLjYyNSIsInBrIjoxOSwibG5fdXJsIjpudWxsLCJpc192ZXJpZmllZCI6ZmFsc2UsImVtYWlsIjoic2Fuam9nc3RoYTdAZ21haWwuY29tIiwiaXNfYWN0aXZlIjpmYWxzZSwicHJfdG9rZW4iOm51bGwsInBob25lIjpudWxsLCJpc19hZG1pbiI6ZmFsc2UsImlzX2JvYXJkX21lbWJlciI6ZmFsc2UsImFkZHJlc3MiOm51bGwsInBvc3QiOm51bGwsInBhc3N3b3JkIjoicGJrZGYyX3NoYTI1NiQyMDAwMCQzeEFUOHgxbkNHSjUkbzBtUlBLOHR5ZjdSMzRncUFSdE9XRkc0aUZYY2Q5TzJiWll2TGZML0FXND0iLCJnaXRodWIiOm51bGwsImZiX3VybCI6bnVsbCwidXJsIjpudWxsLCJ0d191cmwiOm51bGx9.eYAe2oOpILrNtWR6AuFbwvWr2NDjZD1SZ_bTbWeVYFQ",
        "pk": 19
    }, {
        "google": None,
        "ev_token": "f08171d7ffb611b707cf7da1",
        "last_name": None,
        "post_type": "ME",
        "tw_url": None,
        "first_name": "Shovit Thapa",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "shovitthapa@gmail.com",
        "is_active": False,
        "pr_token": None,
        "phone": None,
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$D7twNFtOztzF$VCxxI1D9cI0SdnGpPPRkMwPWN/G4nhQt9sLTDM5H4pM=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOm51bGwsImV2X3Rva2VuIjoiZjA4MTcxZDdmZmI2MTFiNzA3Y2Y3ZGExIiwibGFzdF9uYW1lIjpudWxsLCJwb3N0X3R5cGUiOiJNRSIsInNreXBlIjpudWxsLCJmaXJzdF9uYW1lIjoiU2hvdml0IFRoYXBhIiwiZGF0ZV9vZl9iaXJ0aCI6bnVsbCwibGFzdF9sb2dpbiI6IjIwMTYtMTAtMDZUMjI6MjU6NTcuMjc0IiwicGsiOjIwLCJsbl91cmwiOm51bGwsImlzX3ZlcmlmaWVkIjpmYWxzZSwiZW1haWwiOiJzaG92aXR0aGFwYUBnbWFpbC5jb20iLCJpc19hY3RpdmUiOmZhbHNlLCJwcl90b2tlbiI6bnVsbCwicGhvbmUiOm51bGwsImlzX2FkbWluIjpmYWxzZSwiaXNfYm9hcmRfbWVtYmVyIjpmYWxzZSwiYWRkcmVzcyI6bnVsbCwicG9zdCI6bnVsbCwicGFzc3dvcmQiOiJwYmtkZjJfc2hhMjU2JDIwMDAwJEQ3dHdORnRPenR6RiRWQ3h4STFEOWNJMFNkbkdwUFBSa013UFdOL0c0bmhRdDlzTFRETTVINHBNPSIsImdpdGh1YiI6bnVsbCwiZmJfdXJsIjpudWxsLCJ1cmwiOm51bGwsInR3X3VybCI6bnVsbH0.zV1bbHqdc50C2uwciEhmnGbHLJy7Dbha_hibcbPkSyU",
        "pk": 20
    }, {
        "google": None,
        "ev_token": "a93be6aed59f4bec157951a9",
        "last_name": None,
        "post_type": "ME",
        "tw_url": None,
        "first_name": "Deepak",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "dpanta@abo.fi",
        "is_active": False,
        "pr_token": None,
        "phone": None,
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$uOqNI6A4Cy6f$jVy+PBfa484XTZpRyxznJOgnQv54TnASKmCN/gPMOZc=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOm51bGwsImV2X3Rva2VuIjoiYTkzYmU2YWVkNTlmNGJlYzE1Nzk1MWE5IiwibGFzdF9uYW1lIjpudWxsLCJwb3N0X3R5cGUiOiJNRSIsInNreXBlIjpudWxsLCJmaXJzdF9uYW1lIjoiRGVlcGFrIiwiZGF0ZV9vZl9iaXJ0aCI6bnVsbCwibGFzdF9sb2dpbiI6IjIwMTYtMTAtMDdUMTQ6MjA6NDcuMjkzIiwicGsiOjIxLCJsbl91cmwiOm51bGwsImlzX3ZlcmlmaWVkIjpmYWxzZSwiZW1haWwiOiJkcGFudGFAYWJvLmZpIiwiaXNfYWN0aXZlIjpmYWxzZSwicHJfdG9rZW4iOm51bGwsInBob25lIjpudWxsLCJpc19hZG1pbiI6ZmFsc2UsImlzX2JvYXJkX21lbWJlciI6ZmFsc2UsImFkZHJlc3MiOm51bGwsInBvc3QiOm51bGwsInBhc3N3b3JkIjoicGJrZGYyX3NoYTI1NiQyMDAwMCR1T3FOSTZBNEN5NmYkalZ5K1BCZmE0ODRYVFpwUnl4em5KT2duUXY1NFRuQVNLbUNOL2dQTU9aYz0iLCJnaXRodWIiOm51bGwsImZiX3VybCI6bnVsbCwidXJsIjpudWxsLCJ0d191cmwiOm51bGx9.WGllb3O-pWn0QSZoif7yxgCFfqOTUFHgL6JLCYFfA94",
        "pk": 21
    }, {
        "google": "",
        "ev_token": "",
        "last_name": "",
        "post_type": "ME",
        "tw_url": "",
        "first_name": "Sharmila Yadav",
        "date_of_birth": None,
        "ln_url": "",
        "is_verified": True,
        "email": "ydv.sharmila@gmail.com",
        "is_active": True,
        "pr_token": "",
        "phone": "",
        "is_admin": False,
        "is_board_member": False,
        "address": "",
        "post": None,
        "password": "d84cdb668ae6ba4872a3bbae9639d3cc",
        "skype": "",
        "github": "",
        "fb_url": "",
        "url": "",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaWVsZHMiOnsiZ29vZ2xlIjoiIiwiZXZfdG9rZW4iOiIiLCJsYXN0X25hbWUiOiIiLCJwb3N0X3R5cGUiOiJNRSIsInNreXBlIjoiIiwiZmlyc3RfbmFtZSI6IlNoYXJtaWxhIFlhZGF2IiwiZGF0ZV9vZl9iaXJ0aCI6bnVsbCwibG5fdXJsIjoiIiwiaXNfdmVyaWZpZWQiOnRydWUsImVtYWlsIjoieWR2LnNoYXJtaWxhQGdtYWlsLmNvbSIsImlzX2FjdGl2ZSI6dHJ1ZSwicHJfdG9rZW4iOiIiLCJwaG9uZSI6IiIsImlzX2FkbWluIjpmYWxzZSwiaXNfYm9hcmRfbWVtYmVyIjpmYWxzZSwiYWRkcmVzcyI6IiIsInBvc3QiOm51bGwsInBhc3N3b3JkIjoiZDg0Y2RiNjY4YWU2YmE0ODcyYTNiYmFlOTYzOWQzY2MiLCJnaXRodWIiOiIiLCJmYl91cmwiOiIiLCJ1cmwiOiIiLCJ0d191cmwiOiIifSwibW9kZWwiOiJ0bmFhcHAubWVtYmVyIiwicGsiOjIyfQ.pZYweOuKV0ZrhZL277Z9MIINiK5z0vRag92AqmOidCA",
        "pk": 22
    }, {
        "google": None,
        "ev_token": "",
        "last_name": None,
        "post_type": "ME",
        "tw_url": None,
        "first_name": "Sudhir Karki",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "sudhir.karki@turkunepal.fi",
        "is_active": True,
        "pr_token": None,
        "phone": None,
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$KZr6nN3xX3yW$8oDpxEpKloRuB1NF9NPh/JL7JKxKSwDl7bp9N7vqOKM=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": "None",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOm51bGwsImV2X3Rva2VuIjoiIiwibGFzdF9uYW1lIjpudWxsLCJwb3N0X3R5cGUiOiJNRSIsInNreXBlIjpudWxsLCJmaXJzdF9uYW1lIjoiU3VkaGlyIEthcmtpIiwiZGF0ZV9vZl9iaXJ0aCI6bnVsbCwibGFzdF9sb2dpbiI6IjIwMTctMDktMTBUMTU6MDg6MzguNTY3IiwicGsiOjIzLCJsbl91cmwiOm51bGwsImlzX3ZlcmlmaWVkIjpmYWxzZSwiZW1haWwiOiJzdWRoaXIua2Fya2lAdHVya3VuZXBhbC5maSIsImlzX2FjdGl2ZSI6dHJ1ZSwicHJfdG9rZW4iOm51bGwsInBob25lIjpudWxsLCJpc19hZG1pbiI6ZmFsc2UsImlzX2JvYXJkX21lbWJlciI6ZmFsc2UsImFkZHJlc3MiOm51bGwsInBvc3QiOm51bGwsInBhc3N3b3JkIjoicGJrZGYyX3NoYTI1NiQyMDAwMCRLWnI2bk4zeFgzeVckOG9EcHhFcEtsb1J1QjFORjlOUGgvSkw3Skt4S1N3RGw3YnA5Tjd2cU9LTT0iLCJnaXRodWIiOm51bGwsImZiX3VybCI6bnVsbCwidXJsIjoiTm9uZSIsInR3X3VybCI6bnVsbH0.qkA_uUXn_WMjuzJeM4gZg1okGmDhG360XzeNjIauUFA",
        "pk": 23
    }, {
        "google": "",
        "ev_token": "",
        "last_name": "",
        "post_type": "BM",
        "tw_url": "",
        "first_name": "Ananda Tiwari",
        "date_of_birth": None,
        "ln_url": "",
        "is_verified": True,
        "email": "tiwariananda@yahoo.com",
        "is_active": True,
        "pr_token": "",
        "phone": "",
        "is_admin": False,
        "is_board_member": True,
        "address": "",
        "post": None,
        "password": "asfdsafsadfsadf",
        "skype": "",
        "github": "",
        "fb_url": "",
        "url": "",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOiIiLCJldl90b2tlbiI6IiIsImxhc3RfbmFtZSI6IiIsInBvc3RfdHlwZSI6IkJNIiwic2t5cGUiOiIiLCJmaXJzdF9uYW1lIjoiQW5hbmRhIFRpd2FyaSIsImRhdGVfb2ZfYmlydGgiOm51bGwsImxhc3RfbG9naW4iOiIyMDE3LTA4LTA2VDE5OjQ4OjIxLjgzMCIsInBrIjoyNCwibG5fdXJsIjoiIiwiaXNfdmVyaWZpZWQiOnRydWUsImVtYWlsIjoidGl3YXJpYW5hbmRhQHlhaG9vLmNvbSIsImlzX2FjdGl2ZSI6dHJ1ZSwicHJfdG9rZW4iOm51bGwsInBob25lIjoiIiwiaXNfYWRtaW4iOmZhbHNlLCJpc19ib2FyZF9tZW1iZXIiOmZhbHNlLCJhZGRyZXNzIjoiIiwicG9zdCI6bnVsbCwicGFzc3dvcmQiOiJwYmtkZjJfc2hhMjU2JDIwMDAwJEZOYXR1TUZqbHNyRCRUTXp0MFdYN01TMkpybHFBa3psZEROajA2NzhVU2FZeHNTNjBsTjEwVnFZPSIsImdpdGh1YiI6IiIsImZiX3VybCI6IiIsInVybCI6IiIsInR3X3VybCI6IiJ9.sQvFfc1NC6cY1xzCF3iOeHHwNGb2CZpP_TTGxt2vviY",
        "pk": 24
    }, {
        "google": "",
        "ev_token": "",
        "last_name": "Poudel",
        "post_type": "BM",
        "tw_url": "",
        "first_name": "Anup ",
        "date_of_birth": "1984-01-25",
        "ln_url": "",
        "is_verified": True,
        "email": "friek_an@yahoo.com",
        "is_active": True,
        "pr_token": "",
        "phone": "+358452140666",
        "is_admin": False,
        "is_board_member": True,
        "address": "Krööpilänkatu 4 A 11 20610 Turku",
        "post": None,
        "password": "af2bf63aeb92b1b569983693f29013a1",
        "skype": "",
        "github": "",
        "fb_url": "",
        "url": "",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaWVsZHMiOnsiZ29vZ2xlIjoiIiwiZXZfdG9rZW4iOiIiLCJsYXN0X25hbWUiOiJQb3VkZWwiLCJwb3N0X3R5cGUiOiJCTSIsInNreXBlIjoiIiwiZmlyc3RfbmFtZSI6IkFudXAgIiwiZGF0ZV9vZl9iaXJ0aCI6IjE5ODQtMDEtMjUiLCJsbl91cmwiOiIiLCJpc192ZXJpZmllZCI6dHJ1ZSwiZW1haWwiOiJmcmlla19hbkB5YWhvby5jb20iLCJpc19hY3RpdmUiOnRydWUsInByX3Rva2VuIjoiIiwicGhvbmUiOiIrMzU4NDUyMTQwNjY2IiwiaXNfYWRtaW4iOmZhbHNlLCJpc19ib2FyZF9tZW1iZXIiOnRydWUsImFkZHJlc3MiOiJLclx1MDBmNlx1MDBmNnBpbFx1MDBlNG5rYXR1IDQgQSAxMSAyMDYxMCBUdXJrdSIsInBvc3QiOm51bGwsInBhc3N3b3JkIjoiYWYyYmY2M2FlYjkyYjFiNTY5OTgzNjkzZjI5MDEzYTEiLCJnaXRodWIiOiIiLCJmYl91cmwiOiIiLCJ1cmwiOiIiLCJ0d191cmwiOiIifSwibW9kZWwiOiJ0bmFhcHAubWVtYmVyIiwicGsiOjI1fQ.GtbXD9XBP_yFRmbNkUZ4lFm2r5qstgvUDaHy-w5H3I0",
        "pk": 25
    }, {
        "google": None,
        "ev_token": "",
        "last_name": None,
        "post_type": "ME",
        "tw_url": None,
        "first_name": "Santosh",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "lamichhane17@gmail.com",
        "is_active": True,
        "pr_token": None,
        "phone": None,
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$Nxnxi213PH5M$eo3NEVOxmJB76mBvmQ8SAmVdprJF9cKQlLWbaD5aP+A=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOm51bGwsImV2X3Rva2VuIjoiIiwibGFzdF9uYW1lIjpudWxsLCJwb3N0X3R5cGUiOiJNRSIsInNreXBlIjpudWxsLCJmaXJzdF9uYW1lIjoiU2FudG9zaCIsImRhdGVfb2ZfYmlydGgiOm51bGwsImxhc3RfbG9naW4iOiIyMDE3LTA4LTEwVDEzOjM1OjE2LjIwMiIsInBrIjoyNiwibG5fdXJsIjpudWxsLCJpc192ZXJpZmllZCI6ZmFsc2UsImVtYWlsIjoibGFtaWNoaGFuZTE3QGdtYWlsLmNvbSIsImlzX2FjdGl2ZSI6dHJ1ZSwicHJfdG9rZW4iOm51bGwsInBob25lIjpudWxsLCJpc19hZG1pbiI6ZmFsc2UsImlzX2JvYXJkX21lbWJlciI6ZmFsc2UsImFkZHJlc3MiOm51bGwsInBvc3QiOm51bGwsInBhc3N3b3JkIjoicGJrZGYyX3NoYTI1NiQyMDAwMCROeG54aTIxM1BINU0kZW8zTkVWT3htSkI3Nm1Cdm1ROFNBbVZkcHJKRjljS1FsTFdiYUQ1YVArQT0iLCJnaXRodWIiOm51bGwsImZiX3VybCI6bnVsbCwidXJsIjpudWxsLCJ0d191cmwiOm51bGx9.7Id6g7b759AdHLQAOgj3AJnNjetvqN_XoUzmukNxPSY",
        "pk": 26
    }, {
        "google": None,
        "ev_token": "",
        "last_name": None,
        "post_type": "ME",
        "tw_url": None,
        "first_name": "Sanju KC",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "kc_shanj@hotmail.com",
        "is_active": True,
        "pr_token": None,
        "phone": None,
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$TOHM9WqSBtQC$yKL+aAYe8l2Xux1MCv3IF+vJaSw9pqSEpXGuk05WCj0=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaWVsZHMiOnsiZ29vZ2xlIjpudWxsLCJldl90b2tlbiI6IiIsImxhc3RfbmFtZSI6bnVsbCwicG9zdF90eXBlIjoiTUUiLCJza3lwZSI6bnVsbCwiZmlyc3RfbmFtZSI6IlNhbmp1IEtDIiwiZGF0ZV9vZl9iaXJ0aCI6bnVsbCwibG5fdXJsIjpudWxsLCJpc192ZXJpZmllZCI6ZmFsc2UsImVtYWlsIjoia2Nfc2hhbmpAaG90bWFpbC5jb20iLCJpc19hY3RpdmUiOnRydWUsInByX3Rva2VuIjpudWxsLCJwaG9uZSI6bnVsbCwiaXNfYWRtaW4iOmZhbHNlLCJpc19ib2FyZF9tZW1iZXIiOmZhbHNlLCJhZGRyZXNzIjpudWxsLCJwb3N0IjpudWxsLCJwYXNzd29yZCI6InBia2RmMl9zaGEyNTYkMjAwMDAkVE9ITTlXcVNCdFFDJHlLTCthQVllOGwyWHV4MU1DdjNJRit2SmFTdzlwcVNFcFhHdWswNVdDajA9IiwiZ2l0aHViIjpudWxsLCJmYl91cmwiOm51bGwsInVybCI6bnVsbCwidHdfdXJsIjpudWxsfSwibW9kZWwiOiJ0bmFhcHAubWVtYmVyIiwicGsiOjI3fQ.mFUhH7u3NrDSJi5sIPSx04dem_wvutfMjZlC8Hp0LtE",
        "pk": 27
    }, {
        "google": None,
        "ev_token": "",
        "last_name": None,
        "post_type": "ME",
        "tw_url": None,
        "first_name": "Resha Maharjan",
        "date_of_birth": None,
        "ln_url": None,
        "is_verified": False,
        "email": "presharesha@gmail.com",
        "is_active": True,
        "pr_token": None,
        "phone": None,
        "is_admin": False,
        "is_board_member": False,
        "address": None,
        "post": None,
        "password": "pbkdf2_sha256$20000$QtjYcG4F06Su$SB0Cxhz42STMfuh5/fNcfTfIKgJWvWEPZoUyydHmbxo=",
        "skype": None,
        "github": None,
        "fb_url": None,
        "url": None,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJnb29nbGUiOm51bGwsImV2X3Rva2VuIjoiIiwibGFzdF9uYW1lIjpudWxsLCJwb3N0X3R5cGUiOiJNRSIsInNreXBlIjpudWxsLCJmaXJzdF9uYW1lIjoiUmVzaGEgTWFoYXJqYW4iLCJkYXRlX29mX2JpcnRoIjpudWxsLCJsYXN0X2xvZ2luIjoiMjAxNy0wOC0xNVQxMjoyMzo1NC4xOTIiLCJwayI6MjgsImxuX3VybCI6bnVsbCwiaXNfdmVyaWZpZWQiOmZhbHNlLCJlbWFpbCI6InByZXNoYXJlc2hhQGdtYWlsLmNvbSIsImlzX2FjdGl2ZSI6dHJ1ZSwicHJfdG9rZW4iOm51bGwsInBob25lIjpudWxsLCJpc19hZG1pbiI6ZmFsc2UsImlzX2JvYXJkX21lbWJlciI6ZmFsc2UsImFkZHJlc3MiOm51bGwsInBvc3QiOm51bGwsInBhc3N3b3JkIjoicGJrZGYyX3NoYTI1NiQyMDAwMCRRdGpZY0c0RjA2U3UkU0IwQ3hoejQyU1RNZnVoNS9mTmNmVGZJS2dKV3ZXRVBab1V5eWRIbWJ4bz0iLCJnaXRodWIiOm51bGwsImZiX3VybCI6bnVsbCwidXJsIjpudWxsLCJ0d191cmwiOm51bGx9.ZGRBNWo10D1FpCGDJ8LR9fR5oC2uEctsM9YGiYeOddU",
        "pk": 28
    }, {
        "google": "",
        "ev_token": "",
        "last_name": "",
        "post_type": "BM",
        "tw_url": "",
        "first_name": "Pramoj Prakash Shrestha",
        "date_of_birth": None,
        "ln_url": "",
        "is_verified": True,
        "email": "pramojshrestha@gmail.com",
        "is_active": True,
        "pr_token": "",
        "phone": "",
        "is_admin": False,
        "is_board_member": True,
        "address": "",
        "post": None,
        "password": "5c1417fbf250d81a41038c612faaaceb",
        "skype": "",
        "github": "",
        "fb_url": "",
        "url": "",
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaWVsZHMiOnsiZ29vZ2xlIjoiIiwiZXZfdG9rZW4iOiIiLCJsYXN0X25hbWUiOiIiLCJwb3N0X3R5cGUiOiJCTSIsInNreXBlIjoiIiwiZmlyc3RfbmFtZSI6IlByYW1vaiBQcmFrYXNoIFNocmVzdGhhIiwiZGF0ZV9vZl9iaXJ0aCI6bnVsbCwibG5fdXJsIjoiIiwiaXNfdmVyaWZpZWQiOnRydWUsImVtYWlsIjoicHJhbW9qc2hyZXN0aGFAZ21haWwuY29tIiwiaXNfYWN0aXZlIjp0cnVlLCJwcl90b2tlbiI6IiIsInBob25lIjoiIiwiaXNfYWRtaW4iOmZhbHNlLCJpc19ib2FyZF9tZW1iZXIiOnRydWUsImFkZHJlc3MiOiIiLCJwb3N0IjpudWxsLCJwYXNzd29yZCI6IjVjMTQxN2ZiZjI1MGQ4MWE0MTAzOGM2MTJmYWFhY2ViIiwiZ2l0aHViIjoiIiwiZmJfdXJsIjoiIiwidXJsIjoiIiwidHdfdXJsIjoiIn0sIm1vZGVsIjoidG5hYXBwLm1lbWJlciIsInBrIjoyOX0.pkOvakebmsDV5yKGWpXeA8DHVd4hGaeLxv_b1prwjf8",
        "pk": 29
    }],
    "tnaapp.events": [{
        "reference_number": "",
        "expiry_datetime": "2016-08-30T23:59:00",
        "description": "<div><p>TNA,<br>Welcomes all the Nepalese Community of Turku, on the occasion of Teej.We will be celebrating Teej with our Dear, Respected Ladies, with songs and delicious Nepalese Cuisine.</p><strong>Special Attraction of the Event:-</strong><ul><li>Dar</li><li>Nepalese Cuisine</li><li>Teej Songs</li><li>Dance</li></ul><p> Occasion to be together, please come and bring friends and family and Enjoy this Festival with Turku Nepali Family</p>Dead Line 30 August 2016, (Not applicable for new students, Door pay allowed only for new students)<p style=\"font-weight: bold;\"> WELCOME WELCOME WELCOME</p></div>",
        "title": "Teej 2016 with TNA Family",
        "family_price": 12,
        "registration_open": False,
        "children_price": 0,
        "datetime": "2016-09-03T14:30:00",
        "location": "Yo-Kylä 50 A7,  20540 Turku",
        "registration": True,
        "owner": 1,
        "adult_price": 6,
        "pk": 1
    }, {
        "reference_number": "",
        "expiry_datetime": "2015-08-30T23:59:00",
        "description": "<div>On behalf of Gurkha FC and Turku Nepali Association ry,<p>we would cordially like to welcome you all Nepalese residing in Finland to Gurkha 7 - a - side football tournament.We really appreciate each team’ s contribution towards this event and would like to thank you in advance.Main objective of the tournament is to develop the harmony and co - operation between the Nepalese residing in Finland.</p><ol><li>A team must have at least 7 players to participate and maximum 14 players with one official.Each team will provide one referee when their team is not playing.</li><li>Names should be submitted by 26 th of July.</li><li>Tie - sheet publication: 23 rd of July.</li><li>Deadline for team entry: 20 th of July.</li><li>Entry fees: 150 euros for all of the teams.</li></ol><p style=\"font-weight: bold;\">Welcome Turku Nepali Associations Ry</p></div>",
        "title": "Gurkha 7-A-Side Football tournament",
        "family_price": 25,
        "registration_open": False,
        "children_price": 0,
        "datetime": "2016-08-25T10:00:00",
        "location": "Tuureporinkatu 2c, Turku",
        "registration": False,
        "owner": 1,
        "adult_price": 10,
        "pk": 2
    }, {
        "reference_number": "",
        "expiry_datetime": "2015-08-30T23:59:00",
        "description": "<div>Dear All,<p>Turku Nepal Association ry cordially invites all the Nepalese living in Turku region for its Annual General Meeting to be held on Friday, 8 April 2016 at 5.00 PM in Yo Talo(Rehtorinpellonkatu 4 A, 1 st floor meeting hall).</p><p>AgendaElection of New board and dissolving present one.Handling the responsibility to new members.Planning for new events.</p><p style=\"font-weight: bold;\">Welcome Turku Nepali Associations Ry</p></div>",
        "title": "Annual Meeting 2016",
        "family_price": 25,
        "registration_open": False,
        "children_price": 0,
        "datetime": "2016-03-17T17:00:00",
        "location": "Rehtorinpellonkatu 4A, Turku",
        "registration": False,
        "owner": 1,
        "adult_price": 10,
        "pk": 3
    }, {
        "reference_number": "",
        "expiry_datetime": "2015-08-30T23:59:00",
        "description": "<div>Dear All,<br>In association with Turku-Nepal organization we are organizing a charity futsal tournament to raise funds and rebuild a school in Nepal destroyed after the earthquake.<ol><li>The teams have to consist of 6-12 players.</li><li>The maximum amount of teams will be 10 and the minumum 8, so hurry and sign up as soon as possible!</li><li>The tournament will consist of a group stage, semi-final, and final.</li><li>The duration of the tournament will be 7 hours (14:00-21:00).</li></ol><p>Food and drinks will be available to purchase.The entry fee is 100€ per team and has to be transferred to the account mentioned in the registration form.If you want to play but don’t have a team yet, it is possible to sign up as a single person and be teamed up with other single players.To do that, click on the registration link, choose number of players “1” and team name “single”.The fee for single players is 10€.</p><strong>Tournament structure:</strong><br><br>The matches will be 4vs4.The group phase consist of 3 to 4 matches (depending on the amount of teams) and will be held in two courts at the same time: Kellonsoittajankatu and Aurajoen koulu (adresses can be found below).<br><br>If needed, transportation between venues can be arranged.The final and semifinal will take place in Kellonsoittajankatu.Adresses of venues:– Aurajoen koulu (Papinkatu 4, Turku)– Kellonsoittajankadun koulutalo (Kellonsoittajankatu 9, Turku)<br><br>Registration linkFor any further information please contact: markus.manner@edu.turkuamk.fi <br><br>Follow Us On Facebook.It is strictly advised that all players wear indoors shoe while playing.P S : We are also serving food at the venue.<br><br>All the transcation will be done in cash.<p style=\"font-weight: bold;\">Welcome Turku Nepali Associations Ry</p></div>",
        "title": "Futsal Tournament 2015",
        "family_price": 25,
        "registration_open": False,
        "children_price": 0,
        "datetime": "2015-12-05T14:00:00",
        "location": "Papinkatu 4, Turku",
        "registration": False,
        "owner": 1,
        "adult_price": 10,
        "pk": 4
    }, {
        "reference_number": "",
        "expiry_datetime": "2015-08-30T23:59:00",
        "description": "\nOn the auspicious occasion of our festival Dashain, we’r excited to present you दशैं सांझा 2015 at S-Osakunnat ry Kirkkotie 6, 20540 Turku ( near Ekotori). A not-to-be-missed night of #blessings #togetherness #chatting#Nepali Food #unplugged music, dance, drinks and after party sauna.\nEntry Fee is an amount of money that you pay in order to be allowed into दशैं सांझा २०१५ . Which supports us to pay the rent of the venue , food (veg and non-veg) and other arrangements.\n\nPlease find yourself from the following guests categories :-\n    -Per person: 15 euro\n    -New Comers: 7 Euro\n    -Couple: 30 Euro\n    -Family: 40 Euro\n\nBank Details:\nBeneficiary Name: Turku Nepal Association RY\nAccount Number: FI65 1743 3000 0158 61\n\nReference Number: 1009\nThe deadline for the payment is 15th of October 2015. We repeat , it is 15.10.2015 and deadline means deadline.\nAny problems encountered during the payment can be solved without war , keep calm and ask help from the helpline numbers mentioned at the bottom.\nWe expect everyone’s participation and a successful event. Kiitos!!\n\nHelpline no.\n0442057622 Abarta Pandey\n0409672542 Prabin Lama\n0442153924 Limbu Prajil\n0443582410 Amrit Regmi\n0442730868 Nima waiba\n",
        "title": "Annual Dashain Festival 2015",
        "family_price": 25,
        "registration_open": False,
        "children_price": 0,
        "datetime": "2015-10-10T19:00:00",
        "location": "Kirkkotie 6, 20540 Turku",
        "registration": False,
        "owner": 1,
        "adult_price": 10,
        "pk": 5
    }, {
        "reference_number": "",
        "expiry_datetime": "2015-08-30T23:59:00",
        "description": "\nTurku Nepal Association RY\nMinutes of the meeting held on 27.04.2015\nThe meeting was focused on providing relief to our nation in this pain stricken situation created by the biggest natural disaster of all time.\n-In coordination with Finnish Red cross, our volunteers shift were arranged to collect fund by standing in different parts of Turku, starting from today.\n-It was agreed to organize a food selling program on upcoming restaurant day to collect the fund for earthquake relief.\n-A series of sports program were discussed to be organized to collect fund for the Earthquake victims.\n-It was also requested to all the members of TNA to make the further donations in the account of TNA, which is to be used in Nepal under responsible head in a transparent way to maximize its usage.\n-Similarly coordination to be made with various institutions like university, student association, and airlines for more help and support.\n-Furthermore, website of TNA has been started in its initial stage as Turkunepal.fi\n\nOn Behalf of Turku Nepal Association Ry\nKrishna Sitaula\nThe event was sucessfully completed and all the donation colleceted was give to Red Cross.\nThank you all for supporting us in a dire needs.\n",
        "title": "Nepal Relief Fund Collection",
        "family_price": 25,
        "registration_open": False,
        "children_price": 0,
        "datetime": "2015-04-30T10:00:00",
        "location": "Turku",
        "registration": False,
        "owner": 1,
        "adult_price": 10,
        "pk": 6
    }, {
        "reference_number": "",
        "expiry_datetime": "2015-08-30T23:59:00",
        "description": "\nनयाँ बर्ष सम्बन्धी अत्यन्त जरुरी सुचना :-\nकार्यक्रममा सहभागीता जनाउने म्याद सकिएको छ यद्दपी हामीहरु कोही पनि नछुटौन भन्ने मनसाय राख्दछौ तसर्थ,\nक। कार्यक्रम मा सहभागी हुन चाहनुहुन्छ तर तत्काल रकम को जोहो गर्न अथवा खातामा दाखिला गर्न समस्या छ भने, आउदो १० गते सम्मको लागि शुल्क तिर्ने म्याद बढाउन सकिन्छ तर तपाईंले हामीलाई यो सुचना देखेने बित्तिकै सो कुराको जानकारी भने गराउनु पर्नेछ। जानकारी बिनै प्रबेस गर्ने प्रयास गरेमा शुल्क जफत गरी प्रबेस निसेध सम्म गर्न सकिनेछ ।\nख। कार्यक्रममा आफ्नो गतिविधी तथा उपलब्धि, कम्पनी संस्था, परीयोजना वा सामान्य शुभकामना मन्तब्य दिने इच्छा भयमा उक्त मन्तब्यमा उल्लेख गर्नुहुने कुराहरुको मोटामोटी वा दुरुस्त सार प्रतिलिपी उपलब्ध गराइदिनुहुन अनुरोध छ ।\nग। आफ्नो कला प्रस्तुत गर्न वा बिशेष किसिमले सहयोग गर्न चाहनुहुन्छ भने तुरुन्त संपर्क राख्नुहोला ।\n",
        "title": "New Year’s Celebration 2072",
        "family_price": 25,
        "registration_open": False,
        "children_price": 0,
        "datetime": "2015-04-10T22:00:00",
        "location": "Turku",
        "registration": False,
        "owner": 1,
        "adult_price": 10,
        "pk": 7
    }, {
        "reference_number": "1009",
        "expiry_datetime": "2016-10-09T10:10:00",
        "description": "<div>Dear All,<p>On the auspicious occasion of Dashain 2073, Turku Nepal Association Ry would like to wish good health, success, and long life for all Nepalese residing in Turku, Finland and around the GlobeWe would like you all to come and join us in Dashain Dinner and Cultural Night, program organized by TNA Ry, and make it Grand and Huge Success !!</p><h4>Event Attraction</h4><ol><li>Nepalese Cultural Show</li><li>Nepalese Cuisine Main Course:<ul><li>Pulau (Rice fried in Butter)</li><li>Mutton Curry (Veg. Matar Panir)</li><li>Mixed Vegetable curry</li><li>Pickles</li><li>Salad</li><li>Desert</li><li>Nepalese Desert</li></ul></li></ol>Chance to unite with fellow Nepalese !!!!!!!!<p>Happy Vijaya Dashami 2073 Turku Nepal Association Ry Family(P.S Please Register for the Event and Make the necessary payments before the deadline , invoice will be sent to your registration email after registration.  Details of the program structure will also be sent by email.</p><p style=\"font-weight: bold;\">Welcome Turku Nepali Associations Ry</p></div>   <div>श्रीमान ! श्रीमती ! सुश्री!<p>यही आउदो बिजयादशमी २०७३ को पावन अवसरमा सम्पूर्ण नेपाली दाजु-भाई तथा दिदि-बहिनिहरुमा शु-स्वास्थ्य एब्म दिर्घ-आयुको हार्दिक मंगलमय शुभकामना ब्यक्त गर्दछौ | साथै, यस अवसरमा तुर्कु नेपाल अस्सोसियसन रेउु,  द्वारा आयोजना हुनलागेको बडा दशै भोज तथा सान्स्कृतिक  साँझ   कार्यक्रमा यहाँहरु सबैको उपस्थितिकोलागी हार्दिक अनुरोध गर्दछौ|</p><strong>दर्ता अन्तिम मिती : ६ अक्टोबर २०१६|</strong><br>रात्री  भोजको विवरण!!!<br>मान्सहरी खाना:-<ul><li>पुलाउु</li><li>मासुको तरकारी</li><li>मिश्रित  सबजीअचार</li><li>मिठाइं</li></ul>मशाकाहरी खाना:-<ul><li>पुलाउु</li><li>मटर पनिरको तरकारी</li><li>मिश्रित  सबजीअचार</li><li>मिठाइं</li></ul><p>कृपया, दर्ता समय अबधी भित्रै दर्ता गरी सहयोग गर्दिनहुन हार्दिक अनुरोध गर्दछौ !!!बडा दशै २०७३ को हार्दिक मंगलमय शुभकामना!!<br><strong>तुर्कु नेपाल अस्सोसियसन रेउु परिवार|</strong></p></div>",
        "title": "Dashain Dinner and Cultural Night 2073 !! (बडा दशै भोज तथा सान्स्कृतिक  साँझ )",
        "family_price": 30,
        "registration_open": False,
        "children_price": 10,
        "datetime": "2016-10-11T20:30:00",
        "location": "Linnankatu 32, 20100 Turku",
        "registration": True,
        "owner": 4,
        "adult_price": 15,
        "pk": 9
    }, {
        "reference_number": "12345",
        "expiry_datetime": "2016-09-27T15:47:31",
        "description": "<div><p>Dear All,</p><p>As per the request of Many Nepalese Resident of Turku, Turku Nepal Association Ry, will be screening Nepali Movie Black Hen (कालो पोथी ) !This is the first time ever, TNA is organizing this kind of event. We hope you will all enjoy this event and motivate us to do similar events in upcoming days. </p><p>Ticket can be purchased in gates, Ticket Price 8€.<br>(PS Money collected from the event will be used for GOOD CAUSE !! )<br></p><p style=\"font-weight: bold;\">Welcome Turku Nepali Associations Ry</p></div>",
        "title": "कालो पोथी, Movie Screening",
        "family_price": 0,
        "registration_open": False,
        "children_price": 0,
        "datetime": "2016-10-01T22:00:00",
        "location": "Tykistökatu 4, 20520 Turku",
        "registration": False,
        "owner": 4,
        "adult_price": 0,
        "pk": 10
    }, {
        "reference_number": "1009",
        "expiry_datetime": "2016-10-26T23:55:00",
        "description": "<div><p>Turku Nepal Association Welcomes All Nepalese residing in Turku for <strong>शुभ दीपावली एबम देउसी भइलो कार्यक्रम २०७३,</strong> TNAs first edition.</p><p>Truku Nepal Association wishes Happy Deepwali and Bhai Tika to all Nepalese Residing in Turku and in Finland. The short description शुभ दीपावली एबम देउसी भइलो कार्यक्रम २०७३ program form is as :</p><ul><li>Deepawali (Laxmi puja and lightings)</li><li>Prasad Grahan</li><li> Deusi bhailo program</li><li>Light Tihar Food (selroti, puri, achar, *tarkari)</li></ul>Turku Nepal Association Welcomes you all in its First Edition of शुभ दीपावली एबम देउसी भइलो कार्यक्रम २०७३.<p>Please Register by time and Come and Enjoy with Us</p><p style=\"font-weight: bold;\">Welcome Turku Nepali Associations Ry</p></div>",
        "title": "शुभ दीपावली एबम देउसी भइलो कार्यक्रम २०७३ ",
        "family_price": 15,
        "registration_open": False,
        "children_price": 5,
        "datetime": "2016-10-30T19:05:00",
        "location": "Inspehtorinkatu 4, 20540 Turku",
        "registration": True,
        "owner": 4,
        "adult_price": 7,
        "pk": 11
    }, {
        "reference_number": "Teej17 (Message)",
        "expiry_datetime": "2017-08-16T23:55:00",
        "description": "<div><p>TNA, Welcomes all the Nepalese Community of Turku, on the occasion of Teej.We will be celebrating Teej with our Dear, Respected Ladies, with songs and delicious Nepalese Cuisine.</p><p>Special Attraction of the Event:-<br>Dar (Nepalese Cuisine)- Teej Songs & DanceOccasion to be together, please come and bring friends and family and Enjoy this Festival with Turku Nepali Family.</p><br><strong>Door pay allowed only for new students</strong><br><p>WELCOME WELCOME WELCOME !!!!!!!<br>Location: Yo-Kylä 50 A 7Turku, 20540, Finland<br>Turku Nepal Association Ry turkunepal@gmail.com</p></div>",
        "title": "Teej 2017 with TNA Family",
        "family_price": 16,
        "registration_open": False,
        "children_price": 5,
        "datetime": "2017-08-19T14:00:00",
        "location": "Yo-Kylä 50 A 7, 20540 Turku",
        "registration": True,
        "owner": 4,
        "adult_price": 8,
        "pk": 12
    }, {
        "reference_number": "Message : Dashain17",
        "expiry_datetime": "2017-09-26T23:55:00",
        "description": "<div style='padding: 10px; border-right: 1px solid black'><label> Dear All, </label><div><p style='margin: 4px 0'> On the auspicious occasion of Dashain 2074, Turku Nepal Association Ry would like to wish good health, success, and long life for all Nepalese and friends and families, residing in Turku, Finland and around the Globe, We would like to invite All Dear Nepalese, Friends and families of Nepalese to the event. </p><p> Come together to celebrate the festival of victory of Good over evil, the festival of unity and togetherness, the festival of food and joy. Please come together to celebrate Vijaya Dashami Dinner and Cultural Night, program organized by TNA Ry, and Lets enjoy and celebrate this Festival all together under one roof as One as in Homeland, as One Big Family !! </p><div style='display: flex; justify-content: space-around;'><div><label style='font-weight: bold; font-style: italic;'>Main Course</label><ul style='margin: 0;'><li>Pulau (Rice fried in Butter)</li><li>Mutton Curry (Veg. Matar Panir)</li><li>Mixed Vegetable curry</li><li>Pickles</li><li>Salad</li><li>Nepalese Desert</li></ul></div><div><label style='font-weight: bold; font-style: italic;'>Event Attraction</label><ul style='margin: 0;'><li>Nepalese Cultural Show</li><li>Nepalese Cuisine</li></ul></div></div></div><p>PS: Please Register for the Event and Make the necessary payments before the deadline , invoice will be sent to your registration email after registration. Details of the program structure will also be published later, but you can start registration now.</p><p>PS: Paid member of TNA Ry will have 10% discount on the entry fee, so dear paid members, your payment adjustment will be made accordingly.</p></div><div style='padding: 10px'><label> आदरणीय दाजु-भाइ दिदि-बहिनि एबम साथीहरु, </label><div><p style='margin: 4px 0'> यही आउदो बिजयादशमी २०७४ को पावन अवसरमा सम्पूर्ण नेपाली दाजु-भाई तथा दिदि-बहिनिहरुमा शु-स्वास्थ्य एब्म दिर्घ-आयुको हार्दिक मंगलमय शुभकामना ब्यक्त गर्दछौ !!!! साथै, यस अवसरमा तुर्कु नेपाल अस्सोसियसन रेउु, द्वारा आयोजना हुनलागेको बडा दशै भोज तथा सान्स्कृतिक साँझ कार्यक्रमा यहाँहरु सबैको उपस्थितिकोलागी हार्दिक अनुरोध गर्दछौ !!! <br><strong>दर्ता अन्तिम मिती: २५ सेप्तेम्बेर २०१७ !!</strong></p><div style='display: flex; justify-content: space-around;'><div><label style='font-weight: bold; font-style: italic;'>मान्सहरी खाना</label><ul style='margin: 0;'><li>पुलाउु</li><li>मासुको तरकारी</li><li>मिश्रित सबजी</li><li>अचार</li><li>मिठाइं</li></ul></div><div><label style='font-weight: bold; font-style: italic;'>शाकाहरी खाना</label><ul style='margin: 0;'><li>पुलाउु</li><li>मटर पनिरको तरकारी</li><li>मिश्रित सबजी</li><li>अचार</li><li>मिठाइं</li></ul></div></div></div><p> कृपया, दर्ता समय अबधी भित्रै दर्ता गरी सहयोग गर्दिनहुन हार्दिक अनुरोध गर्दछौ !!! बडा दशै २०७३ को हार्दिक मंगलमय शुभकामना !! तुर्कु नेपाल अस्सोसियसन रेउु परिवार |</p></div>",
        "title": "Dashain Dinner and Cultural Night 2074 !! (बडा दशै भोज तथा सान्स्कृतिक साँझ )",
        "family_price": 34,
        "registration_open": True,
        "children_price": 10,
        "datetime": "2017-10-01T19:30:00",
        "location": "Juhlatilat T-Talo,  Vanha Hämeentie 29, 20540 Turku",
        "registration": True,
        "owner": 4,
        "adult_price": 17,
        "pk": 13
    }],
    "tnaapp.gallery": [{
        "owner": 6,
        "description": "Turku is an old capital city of Finland with diverse natural beauty. Let the gallery speak for itself.\r\nPhoto Credit - Aman Yadav",
        "title": "Turku",
        "pk": 1
    }, {
        "owner": 6,
        "description": "New Year 2072 celebration program organised by the Turku Nepali Association.",
        "title": "New Year 2072",
        "pk": 2
    }, {
        "owner": 6,
        "description": "Dashain 2015 celebration program organised by the Turku Nepali Association.",
        "title": "Dashain 2015",
        "pk": 3
    }, {
        "owner": 6,
        "description": "Earthquake Fund Raise program organised by the Turku Nepali Association.",
        "title": "Earthquake Fund Raise",
        "pk": 4
    }, {
        "owner": 6,
        "description": "Futsal tournament organised by FC Gurkha and TNA.",
        "title": "Football tournament 2015",
        "pk": 5
    }, {
        "owner": 6,
        "description": "Turku 2016 fall at its best.\r\nPhoto Credit - Aman Yadav",
        "title": "Turku 2016",
        "pk": 6
    }, {
        "owner": 4,
        "description": "Dashain Dinner and Cultural Night 2073 !! (बडा दशै भोज तथा सान्स्कृतिक साँझ )",
        "title": "Dashain 2073, Blu Marina",
        "pk": 7
    }],
    "tnaapp.profilepictures": [{
        "owner": 6,
        "url": "members/6/276.png",
        "pk": 1
    }, {
        "owner": 3,
        "url": "members/3/barun.jpg",
        "pk": 2
    }, {
        "owner": 2,
        "url": "members/2/sudhir.jpg",
        "pk": 3
    }, {
        "owner": 4,
        "url": "members/4/hari.jpg",
        "pk": 4
    }, {
        "owner": 5,
        "url": "members/5/nima.jpg",
        "pk": 5
    }, {
        "owner": 9,
        "url": "members/9/33.png",
        "pk": 6
    }, {
        "owner": 18,
        "url": "members/18/nice pic.jpg",
        "pk": 7
    }, {
        "owner": 24,
        "url": "members/24/IMG_1086.JPG",
        "pk": 8
    }, {
        "owner": 25,
        "url": "members/25/845.png",
        "pk": 154
    }, {
        "owner": 22,
        "url": "members/22/94.png",
        "pk": 155
    }],
    "tnaapp.gallerypictures": [{
        "url": "gallery/1/1.jpg",
        "cover_photo": "",
        "gallery": 1,
        "pk": 1
    }, {
        "url": "gallery/1/2.jpg",
        "cover_photo": "gallery/1/2.jpg",
        "gallery": 1,
        "pk": 2
    }, {
        "url": "gallery/1/3.jpg",
        "cover_photo": "",
        "gallery": 1,
        "pk": 3
    }, {
        "url": "gallery/1/4.jpg",
        "cover_photo": "",
        "gallery": 1,
        "pk": 4
    }, {
        "url": "gallery/1/6.jpg",
        "cover_photo": "",
        "gallery": 1,
        "pk": 5
    }, {
        "url": "gallery/1/9.jpg",
        "cover_photo": "",
        "gallery": 1,
        "pk": 6
    }, {
        "url": "gallery/1/11.jpg",
        "cover_photo": "",
        "gallery": 1,
        "pk": 7
    }, {
        "url": "gallery/1/12.jpg",
        "cover_photo": "",
        "gallery": 1,
        "pk": 8
    }, {
        "url": "gallery/1/13.jpg",
        "cover_photo": "",
        "gallery": 1,
        "pk": 9
    }, {
        "url": "gallery/1/14.jpg",
        "cover_photo": "",
        "gallery": 1,
        "pk": 10
    }, {
        "url": "gallery/2/10515202_1082848955075667_8256659570944682426_o-1024x679.jpg",
        "cover_photo": "",
        "gallery": 2,
        "pk": 11
    }, {
        "url": "gallery/2/10547378_1082848408409055_6759579132974971319_o-679x1024.jpg",
        "cover_photo": "",
        "gallery": 2,
        "pk": 12
    }, {
        "url": "gallery/2/10603891_1082847621742467_6315431162688425157_o-1024x679.jpg",
        "cover_photo": "gallery/2/10603891_1082847621742467_6315431162688425157_o-1024x679.jpg",
        "gallery": 2,
        "pk": 13
    }, {
        "url": "gallery/2/10945143_1082849105075652_3247024150555922030_o-1024x679.jpg",
        "cover_photo": "",
        "gallery": 2,
        "pk": 14
    }, {
        "url": "gallery/2/11038862_1082847818409114_7474978249322944989_o-1024x679.jpg",
        "cover_photo": "",
        "gallery": 2,
        "pk": 15
    }, {
        "url": "gallery/2/11096392_1082848831742346_5943466099946640210_o-1024x679.jpg",
        "cover_photo": "",
        "gallery": 2,
        "pk": 16
    }, {
        "url": "gallery/2/11113395_1082847695075793_2311206323086630614_o-1024x679.jpg",
        "cover_photo": "",
        "gallery": 2,
        "pk": 17
    }, {
        "url": "gallery/2/11136154_1082848581742371_6235156797757246792_o-1024x679.jpg",
        "cover_photo": "",
        "gallery": 2,
        "pk": 18
    }, {
        "url": "gallery/2/11149704_1082848651742364_1399525157132578795_o-1024x679.jpg",
        "cover_photo": "",
        "gallery": 2,
        "pk": 19
    }, {
        "url": "gallery/3/11015838_1201002673260294_316030306793721538_o-1024x678.jpg",
        "cover_photo": "",
        "gallery": 3,
        "pk": 20
    }, {
        "url": "gallery/3/11058271_1201505386543356_2198233925982719350_o-1024x678.jpg",
        "cover_photo": "",
        "gallery": 3,
        "pk": 21
    }, {
        "url": "gallery/3/12045348_1201002359926992_964247141634693872_o-1024x678.jpg",
        "cover_photo": "",
        "gallery": 3,
        "pk": 22
    }, {
        "url": "gallery/3/12045729_1201001383260423_7214511617270226006_o-1024x678.jpg",
        "cover_photo": "",
        "gallery": 3,
        "pk": 23
    }, {
        "url": "gallery/3/12052550_1201001599927068_2705198928006295043_o-1024x678.jpg",
        "cover_photo": "",
        "gallery": 3,
        "pk": 24
    }, {
        "url": "gallery/3/12183781_1201002033260358_3185787978209998167_o-1024x678.jpg",
        "cover_photo": "",
        "gallery": 3,
        "pk": 25
    }, {
        "url": "gallery/3/12183999_1201504516543443_450490393131041738_o-1024x678.jpg",
        "cover_photo": "",
        "gallery": 3,
        "pk": 26
    }, {
        "url": "gallery/3/12184045_1201507979876430_8533156285022771100_o-1024x678.jpg",
        "cover_photo": "",
        "gallery": 3,
        "pk": 27
    }, {
        "url": "gallery/3/12184069_1201506279876600_9202764371465929925_o-1024x678.jpg",
        "cover_photo": "",
        "gallery": 3,
        "pk": 28
    }, {
        "url": "gallery/3/12184096_823431824421110_5264194833614227952_o-1024x681.jpg",
        "cover_photo": "gallery/3/12184096_823431824421110_5264194833614227952_o-1024x681.jpg",
        "gallery": 3,
        "pk": 29
    }, {
        "url": "gallery/3/12186589_1201000653260496_4071657474543992380_o-1024x678.jpg",
        "cover_photo": "",
        "gallery": 3,
        "pk": 30
    }, {
        "url": "gallery/3/12194922_823429624421330_229636091388297652_o-1024x681.jpg",
        "cover_photo": "",
        "gallery": 3,
        "pk": 31
    }, {
        "url": "gallery/4/10404274_10153011499663705_4672400968040841721_n.jpg",
        "cover_photo": "",
        "gallery": 4,
        "pk": 32
    }, {
        "url": "gallery/4/11149637_10152994795579006_7741594338100735987_o-1024x662.jpg",
        "cover_photo": "gallery/4/11149637_10152994795579006_7741594338100735987_o-1024x662.jpg",
        "gallery": 4,
        "pk": 33
    }, {
        "url": "gallery/4/11173408_822307721157603_7996483339657404315_n.jpg",
        "cover_photo": "",
        "gallery": 4,
        "pk": 34
    }, {
        "url": "gallery/5/futsal-tornament-1024x722.jpg",
        "cover_photo": "gallery/5/futsal-tornament-1024x722.jpg",
        "gallery": 5,
        "pk": 35
    }, {
        "url": "gallery/6/Turku.jpg",
        "cover_photo": "gallery/6/Turku.jpg",
        "gallery": 6,
        "pk": 42
    }, {
        "url": "gallery/6/_DSC8388.jpg",
        "cover_photo": None,
        "gallery": 6,
        "pk": 43
    }, {
        "url": "gallery/6/_DSC8367.jpg",
        "cover_photo": None,
        "gallery": 6,
        "pk": 44
    }, {
        "url": "gallery/6/_DSC8195.jpg",
        "cover_photo": None,
        "gallery": 6,
        "pk": 45
    }, {
        "url": "gallery/6/_DSC8184.jpg",
        "cover_photo": None,
        "gallery": 6,
        "pk": 46
    }, {
        "url": "gallery/6/_DSC8172.jpg",
        "cover_photo": None,
        "gallery": 6,
        "pk": 47
    }, {
        "url": "gallery/6/_DSC8178.jpg",
        "cover_photo": None,
        "gallery": 6,
        "pk": 48
    }, {
        "url": "gallery/7/IMG_5446.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 49
    }, {
        "url": "gallery/7/IMG_5447.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 50
    }, {
        "url": "gallery/7/IMG_5450.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 53
    }, {
        "url": "gallery/7/IMG_5451.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 54
    }, {
        "url": "gallery/7/IMG_5453.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 56
    }, {
        "url": "gallery/7/IMG_5454.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 57
    }, {
        "url": "gallery/7/IMG_5456.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 59
    }, {
        "url": "gallery/7/IMG_5457.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 60
    }, {
        "url": "gallery/7/IMG_5458.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 61
    }, {
        "url": "gallery/7/IMG_5459.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 62
    }, {
        "url": "gallery/7/IMG_5460.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 63
    }, {
        "url": "gallery/7/IMG_5461.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 64
    }, {
        "url": "gallery/7/IMG_5462.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 65
    }, {
        "url": "gallery/7/IMG_5463.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 66
    }, {
        "url": "gallery/7/IMG_5464.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 67
    }, {
        "url": "gallery/7/IMG_5465.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 68
    }, {
        "url": "gallery/7/IMG_5466.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 69
    }, {
        "url": "gallery/7/IMG_5467.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 70
    }, {
        "url": "gallery/7/IMG_5468.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 71
    }, {
        "url": "gallery/7/IMG_5469.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 72
    }, {
        "url": "gallery/7/IMG_5470.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 73
    }, {
        "url": "gallery/7/IMG_5471.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 74
    }, {
        "url": "gallery/7/IMG_5472.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 75
    }, {
        "url": "gallery/7/IMG_5473.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 76
    }, {
        "url": "gallery/7/IMG_5474.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 77
    }, {
        "url": "gallery/7/IMG_5475.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 78
    }, {
        "url": "gallery/7/IMG_5476.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 79
    }, {
        "url": "gallery/7/IMG_5477.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 80
    }, {
        "url": "gallery/7/IMG_5478.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 81
    }, {
        "url": "gallery/7/IMG_5479.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 82
    }, {
        "url": "gallery/7/IMG_5480.JPG",
        "cover_photo": "gallery/7/IMG_5480.JPG",
        "gallery": 7,
        "pk": 83
    }, {
        "url": "gallery/7/IMG_5481.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 84
    }, {
        "url": "gallery/7/IMG_5482.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 85
    }, {
        "url": "gallery/7/IMG_5483.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 86
    }, {
        "url": "gallery/7/IMG_5484.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 87
    }, {
        "url": "gallery/7/IMG_5485.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 88
    }, {
        "url": "gallery/7/IMG_5486.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 89
    }, {
        "url": "gallery/7/IMG_5487.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 90
    }, {
        "url": "gallery/7/IMG_5488.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 91
    }, {
        "url": "gallery/7/IMG_5489.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 92
    }, {
        "url": "gallery/7/IMG_5490.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 93
    }, {
        "url": "gallery/7/IMG_5491.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 94
    }, {
        "url": "gallery/7/IMG_5492.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 95
    }, {
        "url": "gallery/7/IMG_5493.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 96
    }, {
        "url": "gallery/7/IMG_5494.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 97
    }, {
        "url": "gallery/7/IMG_5495.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 98
    }, {
        "url": "gallery/7/IMG_5496.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 99
    }, {
        "url": "gallery/7/IMG_5497.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 100
    }, {
        "url": "gallery/7/IMG_5498.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 101
    }, {
        "url": "gallery/7/IMG_5500.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 102
    }, {
        "url": "gallery/7/IMG_5501.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 103
    }, {
        "url": "gallery/7/IMG_5502.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 104
    }, {
        "url": "gallery/7/IMG_5503.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 105
    }, {
        "url": "gallery/7/IMG_5504.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 106
    }, {
        "url": "gallery/7/IMG_5505.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 107
    }, {
        "url": "gallery/7/IMG_5506.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 108
    }, {
        "url": "gallery/7/IMG_5507.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 109
    }, {
        "url": "gallery/7/IMG_5508.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 110
    }, {
        "url": "gallery/7/IMG_5509.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 111
    }, {
        "url": "gallery/7/IMG_5510.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 112
    }, {
        "url": "gallery/7/IMG_5513.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 113
    }, {
        "url": "gallery/7/IMG_5515.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 114
    }, {
        "url": "gallery/7/IMG_5520.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 115
    }, {
        "url": "gallery/7/IMG_5521.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 116
    }, {
        "url": "gallery/7/IMG_5522.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 117
    }, {
        "url": "gallery/7/IMG_5523.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 118
    }, {
        "url": "gallery/7/IMG_5525.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 119
    }, {
        "url": "gallery/7/IMG_5526.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 120
    }, {
        "url": "gallery/7/IMG_5528.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 121
    }, {
        "url": "gallery/7/IMG_5529.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 122
    }, {
        "url": "gallery/7/IMG_5530.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 123
    }, {
        "url": "gallery/7/IMG_5531.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 124
    }, {
        "url": "gallery/7/IMG_5533.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 125
    }, {
        "url": "gallery/7/IMG_5534.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 126
    }, {
        "url": "gallery/7/IMG_5536.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 127
    }, {
        "url": "gallery/7/IMG_5539.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 128
    }, {
        "url": "gallery/7/IMG_5541.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 129
    }, {
        "url": "gallery/7/IMG_5542.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 130
    }, {
        "url": "gallery/7/IMG_5544.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 131
    }, {
        "url": "gallery/7/IMG_5545.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 132
    }, {
        "url": "gallery/7/IMG_5549.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 133
    }, {
        "url": "gallery/7/IMG_5550.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 134
    }, {
        "url": "gallery/7/IMG_5552.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 135
    }, {
        "url": "gallery/7/IMG_5553.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 136
    }, {
        "url": "gallery/7/IMG_5554.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 137
    }, {
        "url": "gallery/7/IMG_5555.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 138
    }, {
        "url": "gallery/7/IMG_5556.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 139
    }, {
        "url": "gallery/7/IMG_5557.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 140
    }, {
        "url": "gallery/7/IMG_5558.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 141
    }, {
        "url": "gallery/7/IMG_5559.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 142
    }, {
        "url": "gallery/7/IMG_5560.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 143
    }, {
        "url": "gallery/7/IMG_5561.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 144
    }, {
        "url": "gallery/7/IMG_5562.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 145
    }, {
        "url": "gallery/7/IMG_5565.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 147
    }, {
        "url": "gallery/7/IMG_5566.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 148
    }, {
        "url": "gallery/7/IMG_5567.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 149
    }, {
        "url": "gallery/7/IMG_5568.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 150
    }, {
        "url": "gallery/7/IMG_5570.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 151
    }, {
        "url": "gallery/7/IMG_5579.JPG",
        "cover_photo": "",
        "gallery": 7,
        "pk": 153
    }],
    "tnaapp.eventattendees": [{
        "total": "15",
        "email_reminder_sent": True,
        "name": "Aman Yadav",
        "no_children": 0,
        "email": "amanpdyadav@gmail.com",
        "phone": "+358440210054",
        "has_paid": True,
        "address": "Yo-Kylä 5D 14",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 28
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "chandra kant nyaupane",
        "no_children": 0,
        "email": "visitchandra122@gmail.com",
        "phone": "+358469002925",
        "has_paid": True,
        "address": "yo-kylä",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 29
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Prajil Limbu",
        "no_children": 0,
        "email": "limbuprajil@yahoo.com",
        "phone": "+358442153924",
        "has_paid": True,
        "address": "Yo-kyla 4 C 9",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 30
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "HARI KRISHNA MAHAT",
        "no_children": 0,
        "email": "hmahat@gmail.com",
        "phone": "0449882332",
        "has_paid": True,
        "address": "Yo-kylä 76 A 8",
        "no_family": "0",
        "no_adults": "2",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 31
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "Kalyan giri",
        "no_children": 0,
        "email": "kalyangiri@hotmail.com",
        "phone": "0456489705",
        "has_paid": True,
        "address": "Yo-Kyla 58 A 18",
        "no_family": "0",
        "no_adults": "2",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 32
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "Mahahamad Qaium Shah",
        "no_children": 0,
        "email": "qaiumshah92@gmail.com",
        "phone": "0440389292",
        "has_paid": True,
        "address": "Piinokankuja 4 A 11",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 33
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Manabi poudel",
        "no_children": 0,
        "email": "manabi398@gmail.com",
        "phone": "0413671113",
        "has_paid": True,
        "address": "Honkaharjunkatu 2 C 21",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 34
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "Keshav Thapa",
        "no_children": 0,
        "email": "spandankeshav@gmail.com",
        "phone": "0440568136",
        "has_paid": True,
        "address": "Yo - kylä 8 b 14 20540 Turku",
        "no_family": "0",
        "no_adults": "2",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 35
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Sujan Pokharel",
        "no_children": 0,
        "email": "pokharelsujan134@gmail.com",
        "phone": "+358465663722",
        "has_paid": True,
        "address": "yo-kyla",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 1,
        "events": 9,
        "pk": 36
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Bibek Acharya",
        "no_children": 0,
        "email": "bibwt@yahoo.com",
        "phone": "+358409697061",
        "has_paid": True,
        "address": "Pormestarinkatu 4 I 74",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 37
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Narayan Prasad Pokhrel",
        "no_children": 0,
        "email": "narayan.pokhrel8@gmail.com",
        "phone": "+358400969255",
        "has_paid": True,
        "address": "pormestarinkatu 4",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 38
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "prabin lama",
        "no_children": 0,
        "email": "prabin_lama33@hotmail.com",
        "phone": "+358409672542",
        "has_paid": True,
        "address": "yo-kylä 8c 18",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 39
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Ganga Dhwaj Lingden",
        "no_children": 0,
        "email": "lingden.ganga@gmail.com",
        "phone": "0442005386",
        "has_paid": True,
        "address": "Töykkälänkatu 17 B 203 ",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 41
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Barun Bashyal",
        "no_children": 0,
        "email": "barun@smartmobe.fi",
        "phone": "+358 451147323",
        "has_paid": True,
        "address": "Humalistonkatu 3B A 10 20100 Turku",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 42
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Sunil",
        "no_children": 0,
        "email": "itsme.sunil22@gmail.com",
        "phone": "0409618565",
        "has_paid": True,
        "address": "Savonkedonkatu",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 43
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Anna Lehtonen",
        "no_children": 0,
        "email": "anna.lehtonen@ehja.fi",
        "phone": "0405727480",
        "has_paid": True,
        "address": "Kuivelantie 6 as. 6",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 1,
        "events": 9,
        "pk": 44
    }, {
        "total": "45",
        "email_reminder_sent": True,
        "name": "Krishna sitaula",
        "no_children": 0,
        "email": "krishnasitaula@yahoo.com",
        "phone": "0400771650",
        "has_paid": True,
        "address": "Turku",
        "no_family": "0",
        "no_adults": "3",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 47
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "dipendra karki",
        "no_children": 0,
        "email": "karkideepen@yahoo.com",
        "phone": "0449871737",
        "has_paid": True,
        "address": "turku",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 48
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "Lok",
        "no_children": 0,
        "email": "khanalok@hotmail.com",
        "phone": "0451032820",
        "has_paid": True,
        "address": "Yo-kyla 4A 29",
        "no_family": "0",
        "no_adults": "2",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 49
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "bikram pangeni",
        "no_children": 0,
        "email": "bikrampangeni85@gmail.com",
        "phone": "+358465685872",
        "has_paid": True,
        "address": "yo-kyla 8c,07",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 50
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "Anup Poudel",
        "no_children": 0,
        "email": "anuppou@utu.fi",
        "phone": "0417084546",
        "has_paid": True,
        "address": "Krööpilänkatu 4 A 11",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 51
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Thaman Chand",
        "no_children": 0,
        "email": "thaman.me@gmail.com",
        "phone": "+358442105570",
        "has_paid": True,
        "address": "Maariankatu 2 B 39",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 52
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Anil Dhakal",
        "no_children": 0,
        "email": "tcrush.neil@gmail.com",
        "phone": "0445332882",
        "has_paid": True,
        "address": "yö-kylä 76A 8B",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 53
    }, {
        "total": "40",
        "email_reminder_sent": True,
        "name": "Rajeev Kanth",
        "no_children": 1,
        "email": "rajeevkanth7@gmail.com",
        "phone": "0440210074",
        "has_paid": True,
        "address": "Kraatarinkatu 3 D 34",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 54
    }, {
        "total": "40",
        "email_reminder_sent": True,
        "name": "RANJIT SHARMA",
        "no_children": 1,
        "email": "ranjitksharma001@gmail.com",
        "phone": "505250976",
        "has_paid": True,
        "address": "Jaanintie 34A 12, 20540 TURKU",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 55
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Sobhan Niroula",
        "no_children": 0,
        "email": "sobhan_niroula@yahoo.com",
        "phone": "0406641494",
        "has_paid": True,
        "address": "Lintukorventie 2, Espoo",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 56
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "sanjib gurung",
        "no_children": 0,
        "email": "gurung.sanjib@gmail.com",
        "phone": "0447859309",
        "has_paid": True,
        "address": "Töykkälänkatu 17 B 203",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 57
    }, {
        "total": "40",
        "email_reminder_sent": True,
        "name": "Ang Dawa Lama",
        "no_children": 1,
        "email": "adlama@utu.fi",
        "phone": "0403559810",
        "has_paid": True,
        "address": "Kraatarinkatu 3c, 22",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 58
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Junu Shrestha",
        "no_children": 0,
        "email": "junu.shrest@gmail.com",
        "phone": "+358440224196",
        "has_paid": True,
        "address": "Petkeltie 5",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 59
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "¨pramoj prakash shrestha",
        "no_children": 0,
        "email": "pramojshrestha@gmail.com",
        "phone": "0442373313",
        "has_paid": True,
        "address": "Yo-kyla 36 A 4, 20540, Turku",
        "no_family": "0",
        "no_adults": "2",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 60
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Ajit Bahadur thapa",
        "no_children": 0,
        "email": "magarajit330@gmail.com",
        "phone": "+358465685872",
        "has_paid": True,
        "address": "yo-kyla 8c,07",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 62
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Rupesh Chaudhary",
        "no_children": 0,
        "email": "freakyrupesh@yahoo.com",
        "phone": "+358466352198",
        "has_paid": True,
        "address": "Yo-Kylä 4B 17",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 63
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Suman Aryal",
        "no_children": 0,
        "email": "10wazzza@gmail.com",
        "phone": "0466136490",
        "has_paid": True,
        "address": "Yo-Kylä",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 64
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Gaurav Bikram Thapa ",
        "no_children": 0,
        "email": "gauravbthapac@gmail.com",
        "phone": "0465707096",
        "has_paid": True,
        "address": "yo kylä 2D 16",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 65
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "raju paudel",
        "no_children": 0,
        "email": "pdl_rj@yahoo.com",
        "phone": "0451977958",
        "has_paid": True,
        "address": "turku",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 66
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Pasang Nuru Sherpa",
        "no_children": 0,
        "email": "pasangnurushrp8@gmail.com",
        "phone": "0449719370",
        "has_paid": True,
        "address": "Yo-kyla 4A 22",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 67
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "Ramesh Karki",
        "no_children": 0,
        "email": "karki_ram@hotmail.com",
        "phone": "0443260979",
        "has_paid": True,
        "address": "Yo-kylä 6D 32",
        "no_family": "0",
        "no_adults": "2",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 68
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "kishan kc",
        "no_children": 0,
        "email": "kisson007@gmail.com",
        "phone": "0442712401",
        "has_paid": True,
        "address": "Ritzinkuja 1 O 82",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 69
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "Pradip Neupane And Maria Helena Forsblom",
        "no_children": 0,
        "email": "pneupane34@yahoo.com",
        "phone": "+358451883143",
        "has_paid": True,
        "address": "Merimiehenkatu 7B",
        "no_family": "0",
        "no_adults": "2",
        "no_vegetarian": 2,
        "events": 9,
        "pk": 70
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "yakub kapri",
        "no_children": 0,
        "email": "kanchayakub@gmail.com",
        "phone": "+358414815886",
        "has_paid": True,
        "address": "yo-kylä 4B 15",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 71
    }, {
        "total": "40",
        "email_reminder_sent": True,
        "name": "Prakash Bhattarai",
        "no_children": 1,
        "email": "kashgalaxy95@gmail.com",
        "phone": "+358443190488",
        "has_paid": True,
        "address": "Kalanninkatu 3 A 8",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 72
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Purna Bahadur Baral",
        "no_children": 0,
        "email": "sanusarlahi@gmail.com",
        "phone": "0442369743",
        "has_paid": True,
        "address": "yokyla 10C 2",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 73
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "sanjog raj shrestha",
        "no_children": 0,
        "email": "sanjogstha7@gmail.com",
        "phone": "+358440958339",
        "has_paid": True,
        "address": "yo-kylä 4b 31",
        "no_family": "0",
        "no_adults": "2",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 74
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Sunil Paudel",
        "no_children": 0,
        "email": "dabang.sunilp@gmail.com",
        "phone": "0465658690",
        "has_paid": True,
        "address": "5 B 15 yo-kyllä",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 1,
        "events": 9,
        "pk": 75
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Venkat Subramaniam Rathinakannan",
        "no_children": 0,
        "email": "gemini.venkat@gmail.com",
        "phone": "+358449107321",
        "has_paid": True,
        "address": "Yo-kylä , 2C 4",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 76
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Pragesh shrestha",
        "no_children": 0,
        "email": "Shresthapragesh@gmail.com",
        "phone": "0417406784",
        "has_paid": True,
        "address": "Yo-kyla 5b 15",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 77
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Sabnam Shrestha",
        "no_children": 0,
        "email": "sabnam.stha@gmail.com",
        "phone": "0442120554",
        "has_paid": True,
        "address": "Yo-kylä 68 A 13",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 78
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "Shovit Thapa",
        "no_children": 0,
        "email": "shovitthapa@gmail.com",
        "phone": "0417037151",
        "has_paid": True,
        "address": "pihkalankatu 5B 43B",
        "no_family": "0",
        "no_adults": "2",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 79
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Ramesh Ekambaram",
        "no_children": 0,
        "email": "ramcheme@gmail.com",
        "phone": "372-57825654",
        "has_paid": True,
        "address": "Yo KYLA 5D 14",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 80
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "Ajay Maharjan",
        "no_children": 0,
        "email": "ajay1993@hotmail.com",
        "phone": "0445445459",
        "has_paid": True,
        "address": "Ritzinkuja 1j 54",
        "no_family": "0",
        "no_adults": "2",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 81
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Sandesh Tamang",
        "no_children": 0,
        "email": "sandeshyba@gmail.com",
        "phone": "0449766143",
        "has_paid": True,
        "address": "Turku",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 82
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "hamed ahmadinia",
        "no_children": 0,
        "email": "HAMED.AHMADINIA@AOL.COM",
        "phone": "0466595627",
        "has_paid": True,
        "address": "Yo-Kyla 2A 11",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 84
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Muhaimen Karim",
        "no_children": 0,
        "email": "muhaiminkarim55@gmail.com",
        "phone": "0408465000",
        "has_paid": True,
        "address": "Yo-Kyla 2A 11",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 85
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Deepak",
        "no_children": 0,
        "email": "dpanta@abo.fi",
        "phone": "Panta",
        "has_paid": True,
        "address": "Yo-Kylä 5",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 86
    }, {
        "total": "15",
        "email_reminder_sent": True,
        "name": "Abhinay chaudhar",
        "no_children": 0,
        "email": "avi9071@gmail.com",
        "phone": "0449882331",
        "has_paid": True,
        "address": "Yo-kylä 7",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 87
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "Nima",
        "no_children": 0,
        "email": "lama.rakes@gmail.com",
        "phone": "0449882333",
        "has_paid": True,
        "address": "Yo kyla ",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 88
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "Mikael Matias Hynninen & Motisara ",
        "no_children": 0,
        "email": "mikael.hynninen@gmail.com",
        "phone": "044111222",
        "has_paid": True,
        "address": "Turku",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 89
    }, {
        "total": "30",
        "email_reminder_sent": True,
        "name": "Amrit Poudel",
        "no_children": 0,
        "email": "amrit.poudel@hotmail.com",
        "phone": "044 5659111",
        "has_paid": True,
        "address": "rizinkuja",
        "no_family": "0",
        "no_adults": "2",
        "no_vegetarian": 0,
        "events": 9,
        "pk": 90
    }, {
        "total": "16",
        "email_reminder_sent": True,
        "name": "Aman Yadav",
        "no_children": 0,
        "email": "amanpdyadav@gmail.com",
        "phone": "(+358) 044 021 0054",
        "has_paid": True,
        "address": "Yo-Kylä 5D 14",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 1,
        "events": 12,
        "pk": 97
    }, {
        "total": "16",
        "email_reminder_sent": True,
        "name": "Ananda Tiwari",
        "no_children": 0,
        "email": "tiwariananda@yahoo.com",
        "phone": "0442535468",
        "has_paid": True,
        "address": "Yokyla 38 A 9",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 12,
        "pk": 98
    }, {
        "total": "16",
        "email_reminder_sent": True,
        "name": "Sanju Kc",
        "no_children": 0,
        "email": "kc_shanj@hotmail.com",
        "phone": "0405924524",
        "has_paid": True,
        "address": "Kardinaalinkatu 4j 58",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 12,
        "pk": 99
    }, {
        "total": "16",
        "email_reminder_sent": True,
        "name": "Sudhir Karki",
        "no_children": 0,
        "email": "friendlysudhir@yahoo.com",
        "phone": "0440335674",
        "has_paid": True,
        "address": "Pihkalankatu 5A 15",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 12,
        "pk": 100
    }, {
        "total": "16",
        "email_reminder_sent": True,
        "name": "Santosh",
        "no_children": 0,
        "email": "lamichhane17@gmail.com",
        "phone": "0452299070",
        "has_paid": True,
        "address": "Yo kyla 19",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 1,
        "events": 12,
        "pk": 101
    }, {
        "total": "8",
        "email_reminder_sent": True,
        "name": "Resha Maharjan",
        "no_children": 0,
        "email": "presharesha@gmail.com",
        "phone": "442308978",
        "has_paid": True,
        "address": "Yo-kylä, 36 A 4",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 12,
        "pk": 102
    }, {
        "total": "8",
        "email_reminder_sent": True,
        "name": "Sanzeela",
        "no_children": 0,
        "email": "s.pahadipiya@gmail.com",
        "phone": "449738444",
        "has_paid": True,
        "address": "Tavastilankatu 6A 8",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 12,
        "pk": 103
    }, {
        "total": "8",
        "email_reminder_sent": True,
        "name": "Sulochana KC",
        "no_children": 0,
        "email": "sulokc999@gmail.com",
        "phone": "0442374029",
        "has_paid": True,
        "address": "Yo-kyla",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 1,
        "events": 12,
        "pk": 104
    }, {
        "total": "8",
        "email_reminder_sent": True,
        "name": "Arati Ghimire",
        "no_children": 0,
        "email": "arati.ghimire1@gmail.com",
        "phone": "0466377214",
        "has_paid": True,
        "address": "YO-Kylä 82A 27",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 12,
        "pk": 105
    }, {
        "total": "34",
        "email_reminder_sent": False,
        "name": "Jellene Khoh",
        "no_children": 0,
        "email": "jellene4eva@gmail.com",
        "phone": "+358 46 935 1359",
        "has_paid": False,
        "address": "Sävelkuja 1 as 10, 20740 Turku",
        "no_family": "0",
        "no_adults": "2",
        "no_vegetarian": 1,
        "events": 13,
        "pk": 106
    }, {
        "total": "34",
        "email_reminder_sent": False,
        "name": "Kalyan giri",
        "no_children": 0,
        "email": "kalyangiri@hotmail.com",
        "phone": "0456489705",
        "has_paid": False,
        "address": "Yo-Kyla 58 A 18",
        "no_family": "0",
        "no_adults": "2",
        "no_vegetarian": 0,
        "events": 13,
        "pk": 110
    }, {
        "total": "61.2",
        "email_reminder_sent": False,
        "name": "Hari Krishna Mahat",
        "no_children": 0,
        "email": "hmahat@gmail.com",
        "phone": "0449882332",
        "has_paid": True,
        "address": "Kardinaalinkatu 4J 58, 20540 Turku",
        "no_family": "1",
        "no_adults": "2",
        "no_vegetarian": 0,
        "events": 13,
        "pk": 111
    }, {
        "total": "30.6",
        "email_reminder_sent": False,
        "name": "Anup Poudel",
        "no_children": 0,
        "email": "friek_an@yahoo.com",
        "phone": "0452140666",
        "has_paid": False,
        "address": "Krööpilänkatu 4 A 11 20610 Turku",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 13,
        "pk": 112
    }, {
        "total": "17",
        "email_reminder_sent": False,
        "name": "Ganga Lingden",
        "no_children": 0,
        "email": "lingden.ganga@gmail.com",
        "phone": "0442005386",
        "has_paid": True,
        "address": "Rehtorinpellonkatu 4 A 229",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 13,
        "pk": 113
    }, {
        "total": "17",
        "email_reminder_sent": False,
        "name": "Deepak",
        "no_children": 0,
        "email": "lahiripak@gmail.com",
        "phone": "4170395",
        "has_paid": False,
        "address": "yo-kyla 6C",
        "no_family": "0",
        "no_adults": "1",
        "no_vegetarian": 0,
        "events": 13,
        "pk": 114
    }, {
        "total": "30.6",
        "email_reminder_sent": False,
        "name": "AmanYadav",
        "no_children": 0,
        "email": "amanpdyadav@gmail.com",
        "phone": "440210054",
        "has_paid": True,
        "address": "Yo-Kylä 5D 14",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 1,
        "events": 13,
        "pk": 122
    }, {
        "total": "30.6",
        "email_reminder_sent": False,
        "name": "Pramoj Prakash Shrestha",
        "no_children": 0,
        "email": "pramojshrestha@gmail.com",
        "phone": "442373313",
        "has_paid": False,
        "address": "Yo-kyla 36 A 4",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 13,
        "pk": 123
    }, {
        "total": "39.6",
        "email_reminder_sent": False,
        "name": "Rajeev KanthKanth",
        "no_children": 1,
        "email": "rajeevkanth7@gmail.com",
        "phone": "358440210074",
        "has_paid": True,
        "address": "Kraatarinknatu 3 D 34",
        "no_family": "1",
        "no_adults": "0",
        "no_vegetarian": 0,
        "events": 13,
        "pk": 124
    }, {
        "total": "34",
        "email_reminder_sent": False,
        "name": "Vadim Stingaci",
        "no_children": 0,
        "email": "vadim_stingaci@hotmail.com",
        "phone": "465710100",
        "has_paid": True,
        "address": "Turku",
        "no_family": "0",
        "no_adults": "2",
        "no_vegetarian": 0,
        "events": 13,
        "pk": 126
    }],
    "tnaapp.accountfile": [{
        "url": "accounts/Account-Statement17-09-03.PRN",
        "pk": 1
    }, {
        "url": "accounts/Account-Statement17-09-03.PRN",
        "pk": 2
    }],
    "tnaapp.account": [{
        "ref_num": "",
        "month": 2,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "6,90-",
        "year": 2016,
        "day": 3,
        "pk": 205
    }, {
        "ref_num": "",
        "month": 2,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,77-",
        "year": 2016,
        "day": 3,
        "pk": 206
    }, {
        "ref_num": "",
        "month": 2,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,13-",
        "year": 2016,
        "day": 3,
        "pk": 207
    }, {
        "ref_num": "",
        "month": 2,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "6,00-",
        "year": 2016,
        "day": 3,
        "pk": 208
    }, {
        "ref_num": "",
        "month": 2,
        "beneficiary": "Amazon web services",
        "amount": "0,59-",
        "year": 2016,
        "day": 4,
        "pk": 209
    }, {
        "ref_num": "",
        "month": 2,
        "beneficiary": "Turun yliopisto",
        "amount": "30,00-",
        "year": 2016,
        "day": 15,
        "pk": 210
    }, {
        "ref_num": "",
        "month": 7,
        "beneficiary": "Amazon web services",
        "amount": "17,10-",
        "year": 2016,
        "day": 5,
        "pk": 211
    }, {
        "ref_num": "",
        "month": 7,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "7,27-",
        "year": 2016,
        "day": 5,
        "pk": 212
    }, {
        "ref_num": "",
        "month": 7,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,77-",
        "year": 2016,
        "day": 5,
        "pk": 213
    }, {
        "ref_num": "",
        "month": 7,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,39-",
        "year": 2016,
        "day": 5,
        "pk": 214
    }, {
        "ref_num": "",
        "month": 7,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "6,11-",
        "year": 2016,
        "day": 5,
        "pk": 215
    }, {
        "ref_num": "",
        "month": 7,
        "beneficiary": "SHERPA NYIMA DORJE LAMA",
        "amount": "150,00+",
        "year": 2016,
        "day": 21,
        "pk": 216
    }, {
        "ref_num": "1012",
        "month": 7,
        "beneficiary": "RAI MABINDRA",
        "amount": "150,00+",
        "year": 2016,
        "day": 21,
        "pk": 217
    }, {
        "ref_num": "1012",
        "month": 7,
        "beneficiary": "GHIMIRE NABIN",
        "amount": "150,00+",
        "year": 2016,
        "day": 21,
        "pk": 218
    }, {
        "ref_num": "1012",
        "month": 7,
        "beneficiary": "SHRESTHA SANDEEP KUMAR",
        "amount": "150,00+",
        "year": 2016,
        "day": 21,
        "pk": 219
    }, {
        "ref_num": "1012",
        "month": 7,
        "beneficiary": "RAJ KUMAR G.C.",
        "amount": "150,00+",
        "year": 2016,
        "day": 21,
        "pk": 220
    }, {
        "ref_num": "1012",
        "month": 7,
        "beneficiary": "PAUDYAL MADHU",
        "amount": "150,00+",
        "year": 2016,
        "day": 22,
        "pk": 221
    }, {
        "ref_num": "1012",
        "month": 7,
        "beneficiary": "Hong Kong Turku Oy",
        "amount": "169,69-",
        "year": 2016,
        "day": 27,
        "pk": 222
    }, {
        "ref_num": "",
        "month": 1,
        "beneficiary": "Amazon web services",
        "amount": "0,59-",
        "year": 2016,
        "day": 4,
        "pk": 223
    }, {
        "ref_num": "",
        "month": 1,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "24,48-",
        "year": 2016,
        "day": 7,
        "pk": 224
    }, {
        "ref_num": "",
        "month": 1,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,77-",
        "year": 2016,
        "day": 7,
        "pk": 225
    }, {
        "ref_num": "",
        "month": 1,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "14,24-",
        "year": 2016,
        "day": 7,
        "pk": 226
    }, {
        "ref_num": "",
        "month": 1,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "1,75-",
        "year": 2016,
        "day": 7,
        "pk": 227
    }, {
        "ref_num": "",
        "month": 1,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,40-",
        "year": 2016,
        "day": 7,
        "pk": 228
    }, {
        "ref_num": "",
        "month": 1,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "7,32-",
        "year": 2016,
        "day": 7,
        "pk": 229
    }, {
        "ref_num": "",
        "month": 1,
        "beneficiary": "LIMBU PRAJIL",
        "amount": "25,00+",
        "year": 2016,
        "day": 17,
        "pk": 230
    }, {
        "ref_num": "1012",
        "month": 2,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "6,90-",
        "year": 2016,
        "day": 3,
        "pk": 231
    }, {
        "ref_num": "",
        "month": 3,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "7,30-",
        "year": 2016,
        "day": 3,
        "pk": 232
    }, {
        "ref_num": "",
        "month": 3,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,77-",
        "year": 2016,
        "day": 3,
        "pk": 233
    }, {
        "ref_num": "",
        "month": 3,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,20-",
        "year": 2016,
        "day": 3,
        "pk": 234
    }, {
        "ref_num": "",
        "month": 3,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "6,33-",
        "year": 2016,
        "day": 3,
        "pk": 235
    }, {
        "ref_num": "",
        "month": 3,
        "beneficiary": "TAMANG LAMA RAKESH",
        "amount": "12,00+",
        "year": 2016,
        "day": 3,
        "pk": 236
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "CHHETRI BHIM",
        "amount": "12,00+",
        "year": 2016,
        "day": 3,
        "pk": 237
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "TIMILSINA SAJAN",
        "amount": "12,00+",
        "year": 2016,
        "day": 4,
        "pk": 238
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "THAPA KESHAV KUMAR",
        "amount": "12,00+",
        "year": 2016,
        "day": 4,
        "pk": 239
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "SITAULA KRISHNA",
        "amount": "37,00+",
        "year": 2016,
        "day": 5,
        "pk": 240
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "Amazon web services",
        "amount": "0,59-",
        "year": 2016,
        "day": 7,
        "pk": 241
    }, {
        "ref_num": "",
        "month": 3,
        "beneficiary": "TIMILSINA SAJAN",
        "amount": "25,00+",
        "year": 2016,
        "day": 11,
        "pk": 242
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "KHADKA DHRUBA",
        "amount": "12,00+",
        "year": 2016,
        "day": 17,
        "pk": 243
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "LINGDEN GANGA DHWAJ",
        "amount": "12,00+",
        "year": 2016,
        "day": 21,
        "pk": 244
    }, {
        "ref_num": "1012",
        "month": 4,
        "beneficiary": "REGMI AMRIT",
        "amount": "12,00+",
        "year": 2016,
        "day": 2,
        "pk": 245
    }, {
        "ref_num": "1012",
        "month": 4,
        "beneficiary": "GURUNG SANJIB",
        "amount": "12,00+",
        "year": 2016,
        "day": 4,
        "pk": 246
    }, {
        "ref_num": "1012",
        "month": 4,
        "beneficiary": "Amazon web services",
        "amount": "0,56-",
        "year": 2016,
        "day": 5,
        "pk": 247
    }, {
        "ref_num": "",
        "month": 4,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "7,92-",
        "year": 2016,
        "day": 5,
        "pk": 248
    }, {
        "ref_num": "",
        "month": 4,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,77-",
        "year": 2016,
        "day": 5,
        "pk": 249
    }, {
        "ref_num": "",
        "month": 4,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "1,04-",
        "year": 2016,
        "day": 5,
        "pk": 250
    }, {
        "ref_num": "",
        "month": 4,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "6,11-",
        "year": 2016,
        "day": 5,
        "pk": 251
    }, {
        "ref_num": "",
        "month": 5,
        "beneficiary": "Amazon web services",
        "amount": "0,56-",
        "year": 2016,
        "day": 4,
        "pk": 252
    }, {
        "ref_num": "",
        "month": 5,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "7,03-",
        "year": 2016,
        "day": 4,
        "pk": 253
    }, {
        "ref_num": "",
        "month": 5,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,77-",
        "year": 2016,
        "day": 4,
        "pk": 254
    }, {
        "ref_num": "",
        "month": 5,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,26-",
        "year": 2016,
        "day": 4,
        "pk": 255
    }, {
        "ref_num": "",
        "month": 5,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "6,00-",
        "year": 2016,
        "day": 4,
        "pk": 256
    }, {
        "ref_num": "",
        "month": 5,
        "beneficiary": "TAMANG SANDESH",
        "amount": "12,00+",
        "year": 2016,
        "day": 4,
        "pk": 257
    }, {
        "ref_num": "1012",
        "month": 5,
        "beneficiary": "LAMA PRABIN",
        "amount": "12,00+",
        "year": 2016,
        "day": 19,
        "pk": 258
    }, {
        "ref_num": "1012",
        "month": 5,
        "beneficiary": "GHIMIRE BIDHYA SAGAR",
        "amount": "12,00+",
        "year": 2016,
        "day": 19,
        "pk": 259
    }, {
        "ref_num": "1012",
        "month": 5,
        "beneficiary": "TURUN KAUPUNGIN KESKUSVIRASTO",
        "amount": "356,97-",
        "year": 2016,
        "day": 19,
        "pk": 260
    }, {
        "ref_num": "",
        "month": 5,
        "beneficiary": "BHATTARAI PRAKASH",
        "amount": "12,00+",
        "year": 2016,
        "day": 19,
        "pk": 261
    }, {
        "ref_num": "1012",
        "month": 5,
        "beneficiary": "JOSHI AJAYA",
        "amount": "12,00+",
        "year": 2016,
        "day": 23,
        "pk": 262
    }, {
        "ref_num": "1012",
        "month": 5,
        "beneficiary": "BARAL PURNA",
        "amount": "42,00+",
        "year": 2016,
        "day": 27,
        "pk": 263
    }, {
        "ref_num": "1012",
        "month": 5,
        "beneficiary": "GIRI KALYAN",
        "amount": "12,00+",
        "year": 2016,
        "day": 27,
        "pk": 264
    }, {
        "ref_num": "1012",
        "month": 5,
        "beneficiary": "KARKI NINA BETTINA",
        "amount": "12,00+",
        "year": 2016,
        "day": 30,
        "pk": 265
    }, {
        "ref_num": "1012",
        "month": 5,
        "beneficiary": "CHHETRI BHIM",
        "amount": "25,00+",
        "year": 2016,
        "day": 31,
        "pk": 266
    }, {
        "ref_num": "1012",
        "month": 6,
        "beneficiary": "LIMBU PRAJIL",
        "amount": "12,00+",
        "year": 2016,
        "day": 1,
        "pk": 267
    }, {
        "ref_num": "1012",
        "month": 6,
        "beneficiary": "CHHETRI BHUWAN",
        "amount": "12,00+",
        "year": 2016,
        "day": 2,
        "pk": 268
    }, {
        "ref_num": "1012",
        "month": 6,
        "beneficiary": "CHAND THAMAN BAHADUR",
        "amount": "9,99+",
        "year": 2016,
        "day": 2,
        "pk": 269
    }, {
        "ref_num": "1012",
        "month": 6,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "9,35-",
        "year": 2016,
        "day": 3,
        "pk": 270
    }, {
        "ref_num": "",
        "month": 6,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,77-",
        "year": 2016,
        "day": 3,
        "pk": 271
    }, {
        "ref_num": "",
        "month": 6,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "1,17-",
        "year": 2016,
        "day": 3,
        "pk": 272
    }, {
        "ref_num": "",
        "month": 6,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,20-",
        "year": 2016,
        "day": 3,
        "pk": 273
    }, {
        "ref_num": "",
        "month": 6,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "7,21-",
        "year": 2016,
        "day": 3,
        "pk": 274
    }, {
        "ref_num": "",
        "month": 6,
        "beneficiary": "Amazon web services",
        "amount": "17,36-",
        "year": 2016,
        "day": 6,
        "pk": 275
    }, {
        "ref_num": "",
        "month": 6,
        "beneficiary": "LIDL TURKU PITKAMAKI MN16",
        "amount": "21,16-",
        "year": 2016,
        "day": 7,
        "pk": 276
    }, {
        "ref_num": "",
        "month": 7,
        "beneficiary": "SHERPA NYIMA DORJE LAMA",
        "amount": "50,00+",
        "year": 2016,
        "day": 30,
        "pk": 277
    }, {
        "ref_num": "1012",
        "month": 8,
        "beneficiary": "DELI MARKET TURKU",
        "amount": "20,11-",
        "year": 2016,
        "day": 1,
        "pk": 278
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "K SUPERMARKET ANNIKA",
        "amount": "12,93-",
        "year": 2016,
        "day": 1,
        "pk": 279
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "LIDL ITAHARJU MN184",
        "amount": "44,90-",
        "year": 2016,
        "day": 1,
        "pk": 280
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "K SUPERMARKET ANNIKA",
        "amount": "4,20-",
        "year": 2016,
        "day": 1,
        "pk": 281
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "LIDL TURKU KESKUSTA MN257",
        "amount": "17,04-",
        "year": 2016,
        "day": 1,
        "pk": 282
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "TOKMANNI VARISSUO",
        "amount": "13,98-",
        "year": 2016,
        "day": 1,
        "pk": 283
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "PRISMA ITAHARJU",
        "amount": "40,67-",
        "year": 2016,
        "day": 1,
        "pk": 284
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "7,77-",
        "year": 2016,
        "day": 3,
        "pk": 285
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,77-",
        "year": 2016,
        "day": 3,
        "pk": 286
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,78-",
        "year": 2016,
        "day": 3,
        "pk": 287
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "6,22-",
        "year": 2016,
        "day": 3,
        "pk": 288
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "LAMA PRABIN",
        "amount": "50,00-",
        "year": 2016,
        "day": 4,
        "pk": 289
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "Amazon web services",
        "amount": "17,23-",
        "year": 2016,
        "day": 5,
        "pk": 290
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "OVH Hosting Oy",
        "amount": "3,70-",
        "year": 2016,
        "day": 7,
        "pk": 291
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "DEVKOTA KARKI SRIJANA",
        "amount": "170,00+",
        "year": 2016,
        "day": 8,
        "pk": 292
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "HELP NEPAL NETWORK, NEPAL BANG",
        "amount": "500,00-",
        "year": 2016,
        "day": 11,
        "pk": 293
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "Nordea Bank Finland Plc",
        "amount": "6,75-",
        "year": 2016,
        "day": 11,
        "pk": 294
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "OVH",
        "amount": "44,34-",
        "year": 2016,
        "day": 12,
        "pk": 295
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "Nordea Bank Finland Plc",
        "amount": "40,00-",
        "year": 2016,
        "day": 17,
        "pk": 296
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "SHERPA NYIMA DORJE LAMA",
        "amount": "150,00-",
        "year": 2016,
        "day": 19,
        "pk": 297
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "SHERPA NYIMA DORJE LAMA",
        "amount": "50,00-",
        "year": 2016,
        "day": 20,
        "pk": 298
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "MAHAT HARI KRISHNA",
        "amount": "65,00+",
        "year": 2016,
        "day": 22,
        "pk": 299
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "KHANAL LOK",
        "amount": "25,00-",
        "year": 2016,
        "day": 23,
        "pk": 300
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "SHRESTHA JUNU",
        "amount": "6,00+",
        "year": 2016,
        "day": 28,
        "pk": 301
    }, {
        "ref_num": "1067",
        "month": 8,
        "beneficiary": "KAFLE ASTHA",
        "amount": "6,00+",
        "year": 2016,
        "day": 30,
        "pk": 302
    }, {
        "ref_num": "1067",
        "month": 8,
        "beneficiary": "MAHAT SANDHYA",
        "amount": "24,00+",
        "year": 2016,
        "day": 30,
        "pk": 303
    }, {
        "ref_num": "1067",
        "month": 8,
        "beneficiary": "NEUPANE DEEPA",
        "amount": "6,00+",
        "year": 2016,
        "day": 30,
        "pk": 304
    }, {
        "ref_num": "1067",
        "month": 8,
        "beneficiary": "BAIDHYA ELMITA",
        "amount": "6,00+",
        "year": 2016,
        "day": 31,
        "pk": 305
    }, {
        "ref_num": "",
        "month": 8,
        "beneficiary": "KANTH RAJEEV KUMAR",
        "amount": "12,00+",
        "year": 2016,
        "day": 31,
        "pk": 306
    }, {
        "ref_num": "1067",
        "month": 9,
        "beneficiary": "TIWARI A. OR BANJARA TORANTA K",
        "amount": "12,00+",
        "year": 2016,
        "day": 1,
        "pk": 307
    }, {
        "ref_num": "1067",
        "month": 9,
        "beneficiary": "SHARMA RANJIT KUMAR",
        "amount": "12,00+",
        "year": 2016,
        "day": 2,
        "pk": 308
    }, {
        "ref_num": "1067",
        "month": 9,
        "beneficiary": "TAMANG LAMA RAKESH",
        "amount": "12,00+",
        "year": 2016,
        "day": 2,
        "pk": 309
    }, {
        "ref_num": "1067",
        "month": 9,
        "beneficiary": "KARKI SUDHIR",
        "amount": "6,00+",
        "year": 2016,
        "day": 2,
        "pk": 310
    }, {
        "ref_num": "1067",
        "month": 9,
        "beneficiary": "SHRESTHA SANJOG RAJ",
        "amount": "6,00+",
        "year": 2016,
        "day": 3,
        "pk": 311
    }, {
        "ref_num": "1067",
        "month": 9,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "11,08-",
        "year": 2016,
        "day": 5,
        "pk": 312
    }, {
        "ref_num": "",
        "month": 9,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,77-",
        "year": 2016,
        "day": 5,
        "pk": 313
    }, {
        "ref_num": "",
        "month": 9,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "1,88-",
        "year": 2016,
        "day": 5,
        "pk": 314
    }, {
        "ref_num": "",
        "month": 9,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "1,00-",
        "year": 2016,
        "day": 5,
        "pk": 315
    }, {
        "ref_num": "",
        "month": 9,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "7,43-",
        "year": 2016,
        "day": 5,
        "pk": 316
    }, {
        "ref_num": "",
        "month": 9,
        "beneficiary": "K CITYMARKET TURKU RAVATT",
        "amount": "37,15-",
        "year": 2016,
        "day": 5,
        "pk": 317
    }, {
        "ref_num": "",
        "month": 9,
        "beneficiary": "K CITYMARKET TURKU RAVATT",
        "amount": "13,88-",
        "year": 2016,
        "day": 5,
        "pk": 318
    }, {
        "ref_num": "",
        "month": 9,
        "beneficiary": "Amazon web services",
        "amount": "17,33-",
        "year": 2016,
        "day": 5,
        "pk": 319
    }, {
        "ref_num": "",
        "month": 9,
        "beneficiary": "K CITYMARKET TURKU RAVATT",
        "amount": "0,62-",
        "year": 2016,
        "day": 5,
        "pk": 320
    }, {
        "ref_num": "",
        "month": 9,
        "beneficiary": "DELI MARKET TURKU",
        "amount": "16,82-",
        "year": 2016,
        "day": 5,
        "pk": 321
    }, {
        "ref_num": "",
        "month": 9,
        "beneficiary": "LIDL TURKU KESKUSTA MN257",
        "amount": "1,19-",
        "year": 2016,
        "day": 5,
        "pk": 322
    }, {
        "ref_num": "",
        "month": 9,
        "beneficiary": "SHERPA NYIMA DORJE LAMA",
        "amount": "50,00+",
        "year": 2016,
        "day": 5,
        "pk": 323
    }, {
        "ref_num": "1009",
        "month": 9,
        "beneficiary": "SHAH MAHAMAD QAIUM",
        "amount": "30,00+",
        "year": 2016,
        "day": 24,
        "pk": 324
    }, {
        "ref_num": "1009",
        "month": 9,
        "beneficiary": "YADAV AMAN",
        "amount": "15,00+",
        "year": 2016,
        "day": 24,
        "pk": 325
    }, {
        "ref_num": "1009",
        "month": 9,
        "beneficiary": "LINGDEN GANGA DHWAJ",
        "amount": "15,00+",
        "year": 2016,
        "day": 28,
        "pk": 326
    }, {
        "ref_num": "1009",
        "month": 9,
        "beneficiary": "MAHAT HARI KRISHNA",
        "amount": "30,00+",
        "year": 2016,
        "day": 29,
        "pk": 327
    }, {
        "ref_num": "1009",
        "month": 9,
        "beneficiary": "SITAULA KRISHNA",
        "amount": "30,00+",
        "year": 2016,
        "day": 30,
        "pk": 328
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "POUDEL ANUP",
        "amount": "30,00+",
        "year": 2016,
        "day": 1,
        "pk": 329
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "DHAKAL ANIL",
        "amount": "15,00+",
        "year": 2016,
        "day": 1,
        "pk": 330
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "NIROULA SOBHAN",
        "amount": "15,00+",
        "year": 2016,
        "day": 1,
        "pk": 331
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "TIWARI A. OR BANJARA TORANTA K",
        "amount": "8,00+",
        "year": 2016,
        "day": 2,
        "pk": 332
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "CHAND THAMAN BAHADUR",
        "amount": "15,00+",
        "year": 2016,
        "day": 3,
        "pk": 333
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "SHRESTHA JUNU",
        "amount": "15,00+",
        "year": 2016,
        "day": 3,
        "pk": 334
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "ACHARYA BIBEK",
        "amount": "15,00+",
        "year": 2016,
        "day": 3,
        "pk": 335
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "THAPA KESHAV KUMAR",
        "amount": "30,00+",
        "year": 2016,
        "day": 3,
        "pk": 336
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "SHRESTHA PRAMOJ PRAKASH",
        "amount": "30,00+",
        "year": 2016,
        "day": 4,
        "pk": 337
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "LAMA PRABIN",
        "amount": "15,00+",
        "year": 2016,
        "day": 4,
        "pk": 338
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "DEWAN DEEPLY",
        "amount": "40,00+",
        "year": 2016,
        "day": 4,
        "pk": 339
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "KANTH RAJEEV KUMAR",
        "amount": "40,00+",
        "year": 2016,
        "day": 4,
        "pk": 340
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "GURUNG SANJIB",
        "amount": "15,00+",
        "year": 2016,
        "day": 4,
        "pk": 341
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "Amazon web services",
        "amount": "5,22-",
        "year": 2016,
        "day": 5,
        "pk": 342
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "17,51-",
        "year": 2016,
        "day": 5,
        "pk": 343
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,77-",
        "year": 2016,
        "day": 5,
        "pk": 344
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "1,98-",
        "year": 2016,
        "day": 5,
        "pk": 345
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "14,76-",
        "year": 2016,
        "day": 5,
        "pk": 346
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "POKHREL NARAYAN PRASAD",
        "amount": "15,00+",
        "year": 2016,
        "day": 5,
        "pk": 347
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "PAUDEL RAJU",
        "amount": "15,00+",
        "year": 2016,
        "day": 5,
        "pk": 348
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "SHARMA RANJIT KUMAR",
        "amount": "40,00+",
        "year": 2016,
        "day": 5,
        "pk": 349
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "MAHAT SANDHYA",
        "amount": "30,00+",
        "year": 2016,
        "day": 5,
        "pk": 350
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "CHAUDHARY RUPESH",
        "amount": "15,00+",
        "year": 2016,
        "day": 5,
        "pk": 351
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "POUDEL MANABI",
        "amount": "15,00+",
        "year": 2016,
        "day": 5,
        "pk": 352
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "LIMBU PRAJIL",
        "amount": "15,00+",
        "year": 2016,
        "day": 6,
        "pk": 353
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "LEHTONEN ANNA ELINA ADONIKA",
        "amount": "15,00+",
        "year": 2016,
        "day": 5,
        "pk": 354
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "KARKI RAMESH",
        "amount": "30,00+",
        "year": 2016,
        "day": 6,
        "pk": 355
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "THAPA SUNIL",
        "amount": "15,00+",
        "year": 2016,
        "day": 6,
        "pk": 356
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "GHIMIRE ARATI",
        "amount": "30,00+",
        "year": 2016,
        "day": 6,
        "pk": 357
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "NEUPANE PRADIP",
        "amount": "30,00+",
        "year": 2016,
        "day": 6,
        "pk": 358
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "SHERPA PASANG",
        "amount": "15,00+",
        "year": 2016,
        "day": 6,
        "pk": 359
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "KAPRI YAKUB",
        "amount": "15,00+",
        "year": 2016,
        "day": 6,
        "pk": 360
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "BHATTARAI PRAKASH",
        "amount": "30,00+",
        "year": 2016,
        "day": 6,
        "pk": 361
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "BHATTARAI PRAKASH",
        "amount": "10,00+",
        "year": 2016,
        "day": 6,
        "pk": 362
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "ARYAL SUMAN",
        "amount": "30,00+",
        "year": 2016,
        "day": 6,
        "pk": 363
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "SHRESTHA SABNAM",
        "amount": "15,00+",
        "year": 2016,
        "day": 6,
        "pk": 364
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "SHRESTHA SANJOG RAJ",
        "amount": "30,00+",
        "year": 2016,
        "day": 6,
        "pk": 365
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "POKHAREL SUJAN",
        "amount": "15,00+",
        "year": 2016,
        "day": 6,
        "pk": 366
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "THAPA GAURAV",
        "amount": "15,00+",
        "year": 2016,
        "day": 6,
        "pk": 367
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "BUI DANG THAO VY",
        "amount": "30,00+",
        "year": 2016,
        "day": 6,
        "pk": 368
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "BARAL PURNA",
        "amount": "15,00+",
        "year": 2016,
        "day": 6,
        "pk": 369
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "MAHAT HARI KRISHNA",
        "amount": "45,00+",
        "year": 2016,
        "day": 6,
        "pk": 370
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "SITAULA KRISHNA",
        "amount": "15,00+",
        "year": 2016,
        "day": 7,
        "pk": 371
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "PANTA DEEPAK",
        "amount": "15,00+",
        "year": 2016,
        "day": 7,
        "pk": 372
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "CHAUDHARY ABHINAY",
        "amount": "15,00+",
        "year": 2016,
        "day": 7,
        "pk": 373
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "TAMANG SANDESH",
        "amount": "15,00+",
        "year": 2016,
        "day": 9,
        "pk": 374
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "POUDEL AMRIT",
        "amount": "30,00+",
        "year": 2016,
        "day": 9,
        "pk": 375
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "THAPA SHOVIT",
        "amount": "30,00+",
        "year": 2016,
        "day": 9,
        "pk": 376
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "HAMED AHMADINIA",
        "amount": "15,00+",
        "year": 2016,
        "day": 6,
        "pk": 377
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "KARKI DIPENDRA",
        "amount": "30,00+",
        "year": 2016,
        "day": 10,
        "pk": 378
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "SHRESTHA PRAGESH",
        "amount": "15,00+",
        "year": 2016,
        "day": 10,
        "pk": 379
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "PAUDEL SUNIL",
        "amount": "15,00+",
        "year": 2016,
        "day": 10,
        "pk": 380
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "KHANAL LOK",
        "amount": "30,00+",
        "year": 2016,
        "day": 10,
        "pk": 381
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "HYNNINEN MIKAEL MATIAS",
        "amount": "30,00+",
        "year": 2016,
        "day": 7,
        "pk": 382
    }, {
        "ref_num": "1009",
        "month": 10,
        "beneficiary": "Turun Kansallinen Kirjaka",
        "amount": "5,00-",
        "year": 2016,
        "day": 11,
        "pk": 383
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "THAPA SUNIL",
        "amount": "15,00+",
        "year": 2016,
        "day": 11,
        "pk": 384
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "PAHADI SANDEEP",
        "amount": "8,00+",
        "year": 2016,
        "day": 13,
        "pk": 385
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "THAPA KESHAV KUMAR",
        "amount": "5,00+",
        "year": 2016,
        "day": 13,
        "pk": 386
    }, {
        "ref_num": "",
        "month": 10,
        "beneficiary": "SHRESTHA PRAGESH",
        "amount": "20,00+",
        "year": 2016,
        "day": 31,
        "pk": 387
    }, {
        "ref_num": "1012",
        "month": 11,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "23,28-",
        "year": 2016,
        "day": 3,
        "pk": 388
    }, {
        "ref_num": "",
        "month": 11,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,80-",
        "year": 2016,
        "day": 3,
        "pk": 389
    }, {
        "ref_num": "",
        "month": 11,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "11,09-",
        "year": 2016,
        "day": 3,
        "pk": 390
    }, {
        "ref_num": "",
        "month": 11,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "11,39-",
        "year": 2016,
        "day": 3,
        "pk": 391
    }, {
        "ref_num": "",
        "month": 11,
        "beneficiary": "THAPA KESHAV KUMAR",
        "amount": "20,00+",
        "year": 2016,
        "day": 2,
        "pk": 392
    }, {
        "ref_num": "1012",
        "month": 11,
        "beneficiary": "TAMANG SANDESH",
        "amount": "20,00+",
        "year": 2016,
        "day": 21,
        "pk": 393
    }, {
        "ref_num": "",
        "month": 12,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,80-",
        "year": 2016,
        "day": 5,
        "pk": 394
    }, {
        "ref_num": "",
        "month": 12,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "0,26-",
        "year": 2016,
        "day": 5,
        "pk": 395
    }, {
        "ref_num": "",
        "month": 12,
        "beneficiary": "NORDEA BANK FINLAND PLC",
        "amount": "6,00-",
        "year": 2016,
        "day": 5,
        "pk": 396
    }, {
        "ref_num": "",
        "month": 12,
        "beneficiary": "Smartmobe Oy",
        "amount": "450,00-",
        "year": 2016,
        "day": 10,
        "pk": 397
    }, {
        "ref_num": "",
        "month": 12,
        "beneficiary": "HARI KRISHNA MAHAT",
        "amount": "37,00-",
        "year": 2016,
        "day": 10,
        "pk": 398
    }, {
        "ref_num": "",
        "month": 12,
        "beneficiary": "YADAV AMAN",
        "amount": "12,00-",
        "year": 2016,
        "day": 10,
        "pk": 399
    }, {
        "ref_num": "",
        "month": 12,
        "beneficiary": "KARKI SUDHIR",
        "amount": "20,00-",
        "year": 2016,
        "day": 10,
        "pk": 400
    }, {
        "ref_num": "",
        "month": 12,
        "beneficiary": "TAMANG LAMA RAKESH",
        "amount": "100,00-",
        "year": 2016,
        "day": 10,
        "pk": 401
    }, {
        "ref_num": "",
        "month": 12,
        "beneficiary": "MAHAT HARI KRISHNA",
        "amount": "276,00+",
        "year": 2016,
        "day": 9,
        "pk": 402
    }, {
        "ref_num": "",
        "month": 12,
        "beneficiary": "THAPA JITENDRA",
        "amount": "40,00+",
        "year": 2016,
        "day": 16,
        "pk": 403
    }, {
        "ref_num": "1012",
        "month": 12,
        "beneficiary": "TURUN KAUPUNGIN KESKUSVIRASTO",
        "amount": "154,00-",
        "year": 2016,
        "day": 19,
        "pk": 404
    }, {
        "ref_num": "",
        "month": 12,
        "beneficiary": "SITAULA KRISHNA",
        "amount": "20,00+",
        "year": 2016,
        "day": 24,
        "pk": 405
    }, {
        "ref_num": "1012",
        "month": 1,
        "beneficiary": "NORDEA",
        "amount": "8,81-",
        "year": 2017,
        "day": 4,
        "pk": 406
    }, {
        "ref_num": "",
        "month": 1,
        "beneficiary": "NORDEA",
        "amount": "0,80-",
        "year": 2017,
        "day": 4,
        "pk": 407
    }, {
        "ref_num": "",
        "month": 1,
        "beneficiary": "NORDEA",
        "amount": "0,81-",
        "year": 2017,
        "day": 4,
        "pk": 408
    }, {
        "ref_num": "",
        "month": 1,
        "beneficiary": "NORDEA",
        "amount": "1,20-",
        "year": 2017,
        "day": 4,
        "pk": 409
    }, {
        "ref_num": "",
        "month": 1,
        "beneficiary": "NORDEA",
        "amount": "6,00-",
        "year": 2017,
        "day": 4,
        "pk": 410
    }, {
        "ref_num": "",
        "month": 1,
        "beneficiary": "TURUN KAUPUNGIN KESKUSVIRASTO",
        "amount": "136,00-",
        "year": 2017,
        "day": 31,
        "pk": 411
    }, {
        "ref_num": "",
        "month": 2,
        "beneficiary": "NORDEA",
        "amount": "7,33-",
        "year": 2017,
        "day": 3,
        "pk": 412
    }, {
        "ref_num": "",
        "month": 2,
        "beneficiary": "NORDEA",
        "amount": "0,80-",
        "year": 2017,
        "day": 3,
        "pk": 413
    }, {
        "ref_num": "",
        "month": 2,
        "beneficiary": "NORDEA",
        "amount": "0,20-",
        "year": 2017,
        "day": 3,
        "pk": 414
    }, {
        "ref_num": "",
        "month": 2,
        "beneficiary": "NORDEA",
        "amount": "6,33-",
        "year": 2017,
        "day": 3,
        "pk": 415
    }, {
        "ref_num": "",
        "month": 3,
        "beneficiary": "NORDEA",
        "amount": "7,02-",
        "year": 2017,
        "day": 3,
        "pk": 416
    }, {
        "ref_num": "",
        "month": 3,
        "beneficiary": "NORDEA",
        "amount": "0,80-",
        "year": 2017,
        "day": 3,
        "pk": 417
    }, {
        "ref_num": "",
        "month": 3,
        "beneficiary": "NORDEA",
        "amount": "6,22-",
        "year": 2017,
        "day": 3,
        "pk": 418
    }, {
        "ref_num": "",
        "month": 3,
        "beneficiary": "BASNET RUPESH",
        "amount": "20,00+",
        "year": 2017,
        "day": 5,
        "pk": 419
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "LAMA PRABIN",
        "amount": "20,00+",
        "year": 2017,
        "day": 5,
        "pk": 420
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "CHHETRI BHIM",
        "amount": "20,00+",
        "year": 2017,
        "day": 6,
        "pk": 421
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "PANDEY PRABIN",
        "amount": "20,00+",
        "year": 2017,
        "day": 7,
        "pk": 422
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "JOSHI AJAYA",
        "amount": "20,00+",
        "year": 2017,
        "day": 7,
        "pk": 423
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "KHADKA RAPSON",
        "amount": "20,00+",
        "year": 2017,
        "day": 9,
        "pk": 424
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "SUBEDI KISHOR",
        "amount": "20,00+",
        "year": 2017,
        "day": 10,
        "pk": 425
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "TAMANG LAMA RAKESH",
        "amount": "20,00+",
        "year": 2017,
        "day": 10,
        "pk": 426
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "LINGDEN GANGA DHWAJ",
        "amount": "20,00+",
        "year": 2017,
        "day": 11,
        "pk": 427
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "CHAND THAMAN BAHADUR",
        "amount": "20,00+",
        "year": 2017,
        "day": 11,
        "pk": 428
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "SUBEDI RAJAN",
        "amount": "20,00+",
        "year": 2017,
        "day": 10,
        "pk": 429
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "GIRI KALYAN",
        "amount": "20,00+",
        "year": 2017,
        "day": 25,
        "pk": 430
    }, {
        "ref_num": "1012",
        "month": 3,
        "beneficiary": "THAPA KESHAV KUMAR",
        "amount": "20,00+",
        "year": 2017,
        "day": 24,
        "pk": 431
    }, {
        "ref_num": "1012",
        "month": 4,
        "beneficiary": "NORDEA",
        "amount": "8,49-",
        "year": 2017,
        "day": 5,
        "pk": 432
    }, {
        "ref_num": "",
        "month": 4,
        "beneficiary": "NORDEA",
        "amount": "0,80-",
        "year": 2017,
        "day": 5,
        "pk": 433
    }, {
        "ref_num": "",
        "month": 4,
        "beneficiary": "NORDEA",
        "amount": "1,69-",
        "year": 2017,
        "day": 5,
        "pk": 434
    }, {
        "ref_num": "",
        "month": 4,
        "beneficiary": "NORDEA",
        "amount": "6,00-",
        "year": 2017,
        "day": 5,
        "pk": 435
    }, {
        "ref_num": "",
        "month": 4,
        "beneficiary": "K SUPERMARKET ANNIKA",
        "amount": "1,15-",
        "year": 2017,
        "day": 18,
        "pk": 436
    }, {
        "ref_num": "",
        "month": 4,
        "beneficiary": "TOKMANNI VARISSUO",
        "amount": "1,99-",
        "year": 2017,
        "day": 18,
        "pk": 437
    }, {
        "ref_num": "",
        "month": 4,
        "beneficiary": "KHADKA DHRUBA",
        "amount": "20,00+",
        "year": 2017,
        "day": 18,
        "pk": 438
    }, {
        "ref_num": "",
        "month": 5,
        "beneficiary": "NORDEA",
        "amount": "0,80-",
        "year": 2017,
        "day": 4,
        "pk": 439
    }, {
        "ref_num": "",
        "month": 5,
        "beneficiary": "NORDEA",
        "amount": "0,13-",
        "year": 2017,
        "day": 4,
        "pk": 440
    }, {
        "ref_num": "",
        "month": 5,
        "beneficiary": "NORDEA",
        "amount": "6,11-",
        "year": 2017,
        "day": 4,
        "pk": 441
    }, {
        "ref_num": "",
        "month": 6,
        "beneficiary": "OVH",
        "amount": "17,40-",
        "year": 2017,
        "day": 2,
        "pk": 442
    }, {
        "ref_num": "",
        "month": 6,
        "beneficiary": "OVH",
        "amount": "12,40-",
        "year": 2017,
        "day": 2,
        "pk": 443
    }, {
        "ref_num": "",
        "month": 6,
        "beneficiary": "TURUN KAUPUNGIN KESKUSVIRASTO",
        "amount": "419,93-",
        "year": 2017,
        "day": 4,
        "pk": 444
    }, {
        "ref_num": "",
        "month": 6,
        "beneficiary": "NORDEA",
        "amount": "14,24-",
        "year": 2017,
        "day": 5,
        "pk": 445
    }, {
        "ref_num": "",
        "month": 6,
        "beneficiary": "NORDEA",
        "amount": "0,80-",
        "year": 2017,
        "day": 5,
        "pk": 446
    }, {
        "ref_num": "",
        "month": 6,
        "beneficiary": "NORDEA",
        "amount": "13,44-",
        "year": 2017,
        "day": 5,
        "pk": 447
    }, {
        "ref_num": "",
        "month": 6,
        "beneficiary": "K Rauta Skanssi",
        "amount": "3,95-",
        "year": 2017,
        "day": 19,
        "pk": 448
    }, {
        "ref_num": "",
        "month": 6,
        "beneficiary": "LIDL TURKU KESKUSTA MN257",
        "amount": "10,16-",
        "year": 2017,
        "day": 20,
        "pk": 449
    }, {
        "ref_num": "",
        "month": 7,
        "beneficiary": "NORDEA",
        "amount": "7,55-",
        "year": 2017,
        "day": 5,
        "pk": 450
    }, {
        "ref_num": "",
        "month": 7,
        "beneficiary": "NORDEA",
        "amount": "0,80-",
        "year": 2017,
        "day": 5,
        "pk": 451
    }, {
        "ref_num": "",
        "month": 7,
        "beneficiary": "NORDEA",
        "amount": "0,20-",
        "year": 2017,
        "day": 5,
        "pk": 452
    }, {
        "ref_num": "",
        "month": 7,
        "beneficiary": "NORDEA",
        "amount": "6,55-",
        "year": 2017,
        "day": 5,
        "pk": 453
    }]
}


def populateMembers():
    Member.objects.all().delete()
    for mem in data["tnaapp.member"]:
        m = Member(
            id=mem['pk'],
            post=mem['post'],
            post_type=mem['post_type'],
            token=getJWTToken(mem),
            first_name=mem['first_name'],
            last_name=mem['last_name'],
            email=mem['email'],
            password=mem['password'],
            date_of_birth=mem['date_of_birth'],
            address=mem['address'],
            ev_token=mem['ev_token'],
            pr_token=mem['pr_token'],
            phone=mem['phone'],
            url=mem['url'],
            tw_url=mem['tw_url'],
            ln_url=mem['ln_url'],
            fb_url=mem['fb_url'],
            github=mem['github'],
            skype=mem['skype'],
            is_verified=mem['is_verified'],
            is_active=mem['is_active'],
            is_admin=mem['is_admin'],
            is_board_member=mem['is_board_member']
        )
        m.save()
        ProfilePictures(
            owner=m,
            url='/profilepics/ims.jpg'
        ).save()


def populateProfilePictures():
    ProfilePictures.objects.all().delete()
    for pics in data["tnaapp.profilepictures"]:
        ProfilePictures(
            id=pics['pk'],
            owner=Member.objects.get(id=pics['owner']),
            url=pics['url'],
        ).save()


def populateGallery():
    Gallery.objects.all().delete()
    for gallery in data["tnaapp.gallery"]:
        Gallery(
            id=gallery['pk'],
            owner=Member.objects.get(id=gallery['owner']),
            title=gallery['title'],
            description=gallery['description']
        ).save()


def populateGalleryPictures():
    GalleryPictures.objects.all().delete()
    for pics in data["tnaapp.gallerypictures"]:
        GalleryPictures(
            id=pics['pk'],
            gallery=Gallery.objects.get(id=pics['gallery']),
            url=pics['url'],
            cover_photo=pics['cover_photo']
        ).save()


def populateEevents():
    Events.objects.all().delete()
    for event in data["tnaapp.events"]:
        Events(
            id=event['pk'],
            owner=Member.objects.get(id=event['owner']),
            adult_price=event['adult_price'],
            family_price=event['family_price'],
            registration=event['registration'],
            title=event['title'],
            description=event['description'],
            location=event['location'],
            datetime=event['datetime'],
            expiry_datetime=event['expiry_datetime'],
            registration_open=event['registration_open'],
            reference_number=event['reference_number'],
            children_price=event['children_price']
        ).save()


def populateEventAttendees():
    EventAttendees.objects.all().delete()
    for evt in data["tnaapp.eventattendees"]:
        EventAttendees(
            id=evt['pk'],
            events=Events.objects.get(id=evt['events']),
            email=evt['email'],
            name=evt['name'],
            phone=evt['phone'],
            address=evt['address'],
            no_adults=evt['no_adults'],
            no_family=evt['no_family'],
            no_children=evt['no_children'],
            no_vegetarian=evt['no_vegetarian'],
            total=evt['total'],
            has_paid=evt['has_paid'],
            email_reminder_sent=evt['email_reminder_sent'],
        ).save()


def populateAccounts():
    Account.objects.all().delete()
    for acc in data["tnaapp.account"]:
        Account(
            id=acc['pk'],
            beneficiary=acc['beneficiary'],
            ref_num=acc['ref_num'],
            amount=acc['amount'],
            year=acc['year'],
            month=acc['month'],
            day=acc['day']

        ).save()


def generateData(request):
    populateMembers()
    populateProfilePictures()
    populateEevents()
    populateEventAttendees()
    populateGallery()
    populateGalleryPictures()
    populateAccounts()
    return JSONResponse({'message': 'Database populated.'}, status=200)
