from __future__ import print_function

import logging

import sib_api_v3_sdk
from jinja2 import Environment, PackageLoader, select_autoescape
from sib_api_v3_sdk.rest import ApiException

from app.core.settings import settings


def _render_template(template, **kwargs):
    """renders a Jinja template into HTML"""
    env = Environment(
        loader=PackageLoader('app', 'templates'),
        autoescape=select_autoescape(['html', 'xml', 'j2']),
    )
    template = env.get_template(template)
    return template.render(**kwargs)


def send_email(
    email_to: str,
    name_to: str,
    subject: str = '',
    html_template: str = '',
    **kwargs,
):
    if not settings.EMAILS_ENABLED:
        logging.warning('E-mail service disable')
        return False

    html_content = _render_template(html_template, **kwargs)

    to = [{'email': email_to, 'name': name_to}]
    sender = {
        'name': settings.EMAILS_FROM_NAME,
        'email': settings.EMAILS_FROM_EMAIL,
    }
    headers = {'Some-Custom-Name': 'unique-id-1234'}

    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = settings.BREVO_API_KEY

    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration)
    )

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to,
        headers=headers,
        html_content=html_content,
        sender=sender,
        subject=subject,
    )
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        logging.info(api_response)
        return True
    except ApiException as e:
        logging.error(
            'Exception when calling SMTPApi->send_transac_email: %s\n' % e
        )
        return False


def send_test_email(email_to: str) -> None:
    project_name = settings.PROJECT_NAME
    subject = f'{project_name} - Test email'
    send_email(
        email_to,
        'Email tester',
        subject,
        settings.TEMPLATE_TEST,
        project_name=settings.PROJECT_NAME,
        email=email_to,
    )
