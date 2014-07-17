from django import forms
from django.core import mail

from infoorg.models import InfoTip


class InfoTipForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def handle(self):
        self.save_it()
        if self.cleaned_data['cc_myself']:
            self.send_mail()

    def save_it(self):
        it = InfoTip(
            subject=self.cleaned_data['subject'],
            message=self.cleaned_data['message'],
            sender=self.cleaned_data['sender'])
        it.save()

    def send_mail(self):
        sender = self.cleaned_data['sender']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        mail.send_mail(
            'Thanks for Submitting an InfoTip!',
            subject + "\n" + message,
            'from@example.com',
            [sender],
            fail_silently=False)
