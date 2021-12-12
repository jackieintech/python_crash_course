current_users = ['jairme', 'Bignothing', 'galadriel', 'BNfan', 'orion']
new_users = ['bae', 'vic', 'galadriel', 'orion', 'BNfan']

for new_user in new_users:
    if new_user in current_users:
        print(f"The username {new_user.lower()} is taken. Try a different one.")
    else:
        print(f"The username {new_user.lower()} is available. Continue.")
