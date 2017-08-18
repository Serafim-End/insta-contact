# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

from django.shortcuts import render

from forms import PageForm
from models import PageModel
from mail import send_mail

# Create your views here.


def page(request):
    template_name = os.path.join('page', 'subscribe.html')

    if request.method == 'POST':

        form = PageForm(request.POST)
        if form.is_valid():

            form.save()

            o = PageModel.objects.last()

            parameters = {
                'user_list': 'endnikita@gmail.com',
                'attachments': [],
                'subject': 'Personal Data from Instagram'
            }

            info = """
            Добрый день, коллеги! Поступила новая информация, 
            пользователь instagram внес следующие персональные данные для обработки: 
            Имя: %s
            Фамилия: %s
            Телефон: %s
            email: %s
            
            С Уважением, парень который следит за всеми!
            """ % (o.first_name, o.second_name, o.phone_number, o.email)

            parameters['text'] = info
            send_mail(**parameters)
            new_template_name = os.path.join('page', 'detail.html')
            return render(request, new_template_name)

        else:
            form = PageForm()

        print('errors')
    else:
        form = PageForm()
    return render(request, template_name, {'form': form})
