from django import forms
from infoorg.models import InfoTip

class InfoTipForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def send_mail(self):
        it = InfoTip(
            subject=self.cleaned_data['subject'],
            message=self.cleaned_data['message'],
            sender=self.cleaned_data['sender'])
        it.save()
        print "I would totally send mail now"
