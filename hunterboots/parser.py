import requests


url = 'https://hunterboots.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.google.com/',
    'Connection': 'keep-alive',
    'Cookie': 'localization=US; cart_currency=USD; _shopify_y=f2c7055d-1fce-44ba-8c8a-3cdbb5401e31; _shopify_s=214bdef2-63be-45de-b9d7-3f57e119f601; _shopify_analytics=:AZ1wmqWmAAEALTBubq8Tq0rskMHyK3mGLKgXlimU8u2dI865Zx2pIKaD3uMcACvmRGc6sCAcNfIvJ0MtTrGDVl161eTg7a0YuSHRTzI:; _shopify_marketing=:AZ1wmqWmAAEASgRXHx0iHKfZg7I8SmVC_M7m8Ove8JtpIvtP6T7_bJAOuPcei0sf89eXErNG0jB7s1NAi_nwFiKlO-8:; __eventn_id=kt2uhheuwc.1775710676; lePixelVisitorId=v-1775710678050-735153; lePixelSessionId=s-1775710678050-562541; cart=hWNAoQpIZn57oXhQnb7PPtxs%3Fkey%3Df1e8584d6531956c00c46f673e719b51; cjConsent=MHxOfDB8Tnww; cjUser=538da385-8390-4e26-bab8-25def5dcb1a0; shopify_client_id=f2c7055d-1fce-44ba-8c8a-3cdbb5401e31; _pandectes_gdpr=eyJjb3VudHJ5Ijp7ImNvZGUiOiJJTiIsInN0YXRlIjoiR0oiLCJkZXRlY3RlZCI6MTc3NTcxMDY3OX0sInN0YXR1cyI6IiIsInRpbWVzdGFtcCI6bnVsbCwicHJlZmVyZW5jZXMiOm51bGx9; _obv_a_vid=48f21921-abf7-45ff-8bb0-b5de62da3391; _gcl_au=1.1.851113817.1775710680; __kla_id=eyJjaWQiOiJPV0UzTkdFeE5XTXRZekF4TmkwMFpUSTVMV0U1TkdNdE5UTTROR05tWkRZMk5Ua3cifQ==; _fbp=fb.1.1775710680722.1443432755; cebs=1; _ce.clock_data=440%2C45.114.65.131%2C1%2C91e1a2a41c0741f7f47615ab9de2fb8a%2CChrome%2CIN; _tt_enable_cookie=1; _ttp=01KNR9NEKX2H555DTGWM58J0RR_.tt.0; cebsp_=1; _ce.s=v~0662c33bf7845b879373ece6de912311af41109a~lcw~1775710681799~vir~new~lva~1775710680975~vpv~0~v11.cs~439933~v11.s~af9fdde0-33d0-11f1-9ed5-35228465a833~v11.vs~0662c33bf7845b879373ece6de912311af41109a~v11.fsvd~eyJub3RNb2RpZmllZFVybCI6Imh0dHBzOi8vaHVudGVyYm9vdHMuY29tLyIsInVybCI6Imh1bnRlcmJvb3RzLmNvbSIsInJlZiI6IiIsInV0bSI6W119~v11.sla~1775710681799~v11ls~af9fdde0-33d0-11f1-9ed5-35228465a833~lcw~1775710681814; _uetsid=afca875033d011f18d389fb875f2a72e; _uetvid=afca9cb033d011f189863ff1030afcf4; _ga_G8TN3EC7T2=GS2.1.s1775710682$o1$g0$t1775710682$j60$l0$h1764827779; _ga=GA1.1.260000192.1775710682; _shopify_essential=:AZ1wmqWPAAEAa5tJMlopFvxtA1hbSXZgk3unJd7LwHHeYu32GSq-QXr5vITCiE6divJ8C3dAVBW1h6Kd84x5qT_8Ppl1xGRQpyHiFT_teS_Drdmmof0qZ6JR2iEym7HFs4dxz_OPObAT3lWPArj-GqrPdg8haVsQKkUz01sYF4oH7SeDRgOYdQSZTtmiYhfYIMnBfZcvEBVnNYvmPHk1VKcNPZB4jHeOdkTKB4g7EZ6VDcis2euT5YoS42OIgYseaT7PXFWoVbSmLMQbG0Ah74qHVKrfuTEENG9qJVY8O7wI0MirLeAyDFEQi8GO86RuJONJHlJpJ0pzFUAx7RtwKAOUJUY8l_9URPQTNmVqp7Q9XxM8PzDujmb36aAhyqX9-Hnc1_JH_dBTy7xfhNz_kmm5YqBv11xKzmefpFaoYiZz8Qd8OZlB8gp5d3JbidV9Kg3gbCe6ug:; _shg_session_id=7f2de3bb-497c-4293-a4a1-2eedbbb812b5; _shg_user_id=1b6b1d31-18d3-40a0-a00b-7d696e247440; ttcsid=1775710681754::3gSzc6baxhOBWupjStT0.1.1775710691780.0::1.-5564.0::0.0.0.0::8151.7.0; ttcsid_CK3OLDJC77UC9P2VODJ0=1775710681752::rjkKihW9SOignKpiAMVC.1.1775710691784.1'
}


responce = requests.get(url,headers=headers)


if responce.status_code == 200:

    with open('hunter.html','w',encoding='utf-8') as f:
        f.write(responce.text)
    print('Done')
else:
    print('Error!!')
