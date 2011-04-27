from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render_to_response
from django.template import RequestContext
from django.conf import settings

message = """
Es wurde eine neue Anfrage mit dem Schnellhilfe Fomular auf biotech.at abgegeben:

Name: %s
Email: %s
Tel: %s
Grund: %s

"""

def help_request(request, template_name="support_confirm.html"):
    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    tel = request.POST.get("tel", "")
    reason = request.POST.get("reason", "")

    from django.core.mail import EmailMessage
    email = EmailMessage('Schnellhilfe-Anfrage', message%(name, email, tel, reason),
                         to=['office@biotech.at', 'phil@maptales.com'])
    email.send()

    return render_to_response(template_name, {}, RequestContext(request))
