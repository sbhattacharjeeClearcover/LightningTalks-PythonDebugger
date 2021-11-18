from debug_helpers.json_readers import my_json, team_json


def get_de_emails():
    my_data = my_json()['my_details']
    de_team = team_json()
    all_emails = []

    for member in de_team.get('ccde_team'):
        if member.get('name') == my_data.get('first_name'):
            member['email'] = my_data.get('email')
        if '@clearcover.com' in member.get('email'):
            all_emails.append(member.get('email'))
    return all_emails


if __name__ == '__main__':

    # Evaluate Expression and Set Value
    print(get_de_emails())
