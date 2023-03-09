import requests

API_POST_URL = 'https://pastebin.com/api/api_post.php'
DEVELOPER_API_KEY = 'NyB4JV8hBPE7XuwUUkZY24PmXJ6ReKF_'

def main():
    paste_url = post_new_paste('Whatever paste', 'a bunch of crap')
    #pass

def post_new_paste(title, body_text, expiration='10M', listed=True):
    """Creates a new public PasteBin paste

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str, optional): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y). Defaults to '10M'.
        listed (bool, optional): Whether the paste is publicly listed (True) or not (False). Defaults to True.

    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """
    # Create dictionary of parameter values
    params = {
        'api_dev_key': DEVELOPER_API_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if listed else 1
    }

    # Send the POST request to the PasteBin API
    print("Posting new paste to PasteBin...", end='')
    resp_msg = requests.post(API_POST_URL, data=params)

    # Check if paste was created successfully
    if resp_msg.ok:
        print('success')
        #print(f'URL of new paste: {resp_msg.text}')
        return resp_msg.text
    else:
        print("failure")
        print(f"Response code: {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error: {resp_msg.text}")

if __name__ == "__main__":
    main()