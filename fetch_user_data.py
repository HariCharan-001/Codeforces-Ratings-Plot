import requests
data = requests.get('https://codeforces.com/api/user.ratedList')
data = data.json()
data = data['result']

f = open('CF_User_ratings.txt', 'w')

for user in data:
    f.write(str(user['handle']))
    f.write(' ')
    f.write(str(user['rating']))
    f.write('\n')