print('お使いのg-mailアカウントを入力してください ')

gmail_account = str(input())

print('g-mailのパスワードを入力してください')

gmail_pass = str(input())

print('メールの送り先を入力してください')

mail_to = str(input())

print('メールの件名を入力してください')

mail_sub = str(input())

print('メールの本文を入力してください')

mail_text = str(input())

print('送り先 : ' + mail_to )
print('上記の内容で送りますがよろしいですか。/n 「はい」ならば Y を、「いいえ」ならば N を入力してください')

Judge = str(input())

if Judge == 'Y':
	import smtplib
	from email.mime.text import MIMEText
	from email.utils import formatdate


	# Gmailにログイン
	smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpobj.ehlo()
	smtpobj.starttls()
	smtpobj.ehlo()
	smtpobj.login(gmail_account, gmail_pass)

	# メール作成
	msg = MIMEText(mail_text)
	msg['Subject'] = mail_sub
	msg['From'] = gmail_account
	msg['To'] = mail_to
	msg['Date'] = formatdate()



	# メール送信
	smtpobj.sendmail(msg['From'], msg['To'], msg.as_string())
	smtpobj.close()	




