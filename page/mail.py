# coding: utf-8

from datetime import datetime

from sendsay.api import SendsayAPI


def send_mail(**kwargs):
    """
    :param html: rendered message (html version) to send
    :param when: time of send starts
    :param from_email: email of sender
    :param from_name: name of sender
    :param text: text message
    :param user_list: list of the users that should be notified
    :param attachments: files to attach
    :param subject: subject of the mail
    :return: result of delivery
    """

    user_list = kwargs.get('user_list')
    if not user_list:
        raise Exception(' user list should not be empty')

    html = kwargs.get('html')
    text = kwargs.get('text')
    when = datetime.now().strftime('%Y-%m-%d %H:%M')
    from_name = kwargs.get('from_name', 'PrimeConcept')
    from_email = kwargs.get('from_email', 'ne@login.ru')
    attachments = kwargs.get('attachments')
    subject = kwargs.get('subject')

    def track_process(resp, status_msg):
        print('---- %s' % status_msg)

    api = SendsayAPI(login='ne@login.ru',
                     password='oque5Ki')

    issue = {
        'sendwhen': 'later',
        'later.time': when,
        'letter': {
            'subject': subject,
            'from.name': from_name,
            'from.email': from_email,
            'message': {},
        },
        'relink': 1,
        'users.list': (user_list if user_list else from_email),
        'group': 'masssending',
    }

    if html:
        issue['letter']['message']['html'] = html
        if attachments:
            issue['letter']['attaches'] = [
                api.attach_file(e) for e in attachments
            ]

    elif text:
        issue['letter']['message']['text'] = text
    else:
        raise Exception('nothing to send, '
                        'you should include html or text in your letter')

    response = api.request('issue.send', issue)

    # result = api.track_wait(
    #     response,
    #     callback=track_process,
    #     retry_interval=5,
    #     max_attempts=100
    # )
    # print result

    return result